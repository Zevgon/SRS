from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db import transaction
from utils.word_utils import get_words
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User # NOQA


class Bucket(models.Model):
    number = models.IntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        return str(self.number)


class Language(models.Model):
    title = models.CharField(max_length=100)
    title_slug = AutoSlugField(unique=True, populate_from='title')

    def __str__(self):
        return self.title


class Word(models.Model):
    language = models.ForeignKey(Language)
    english = models.CharField(max_length=100)
    foreign = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '%s: %s' % (self.english, self.foreign) + ' (%s)' % self.language # NOQA

    def to_obj(self):
        return {
            'english': self.english,
            'foreign': self.foreign,
            'pronunciation': self.pronunciation,
            'id': self.id
        }

    @classmethod
    def validate_keys(cls, keys, kwargs):
        for key in keys:
            if key not in kwargs:
                raise Exception('Must include %s' % key)

    @classmethod
    def add(cls, **kwargs):
        cls.validate_keys(
            ['language', 'english', 'foreign'], kwargs)
        if type(kwargs['language']) in [str, unicode]:
            try:
                l = Language.objects.get(
                    title_slug=slugify(kwargs['language']))
            except Language.DoesNotExist:
                raise Exception('We don\'t support that language yet')
            kwargs['language'] = l
        cls.objects.create(**kwargs)

    @classmethod
    @transaction.atomic
    def bulk_add(cls, words, language_slug):
        word_kwargs = {}
        try:
            language_obj = Language.objects.get(title_slug=language_slug)
        except Language.DoesNotExist:
            raise Exception('We don\'t support that language yet')
        word_kwargs['language'] = language_obj

        for word in words:
            word_kwargs['english'] = word['english']
            word_kwargs['foreign'] = word['foreign']
            if 'pronunciation' in word:
                word_kwargs['pronunciation'] = word['pronunciation']
            cls.add(**word_kwargs)

    @classmethod
    def import_words(cls, language_slug):
        words = get_words(language_slug)
        cls.bulk_add(words, language_slug)


class WordStats(models.Model):
    word = models.ForeignKey(Word, related_name='word_stats')
    user = models.ForeignKey(User)
    bucket = models.ForeignKey(Bucket, default=1)
    last_reviewed = models.DateTimeField(null=True)
    times_right = models.IntegerField(default=0)
    know_status = models.IntegerField(default=0)

    def __str__(self):
        return '%s, %s' % (self.word.foreign, self.user.username)

    def reset(self):
        self.bucket = Bucket.objects.first()
        self.times_right = 0
        self.know_status = 0
        self.save()

    @classmethod
    def reset_all(cls):
        for ws in cls.objects.all():
            ws.reset()

    @classmethod
    @transaction.atomic
    def set_up_user_with_word_stats(cls, user, language):
        for word in Word.objects.filter(language=language):
            cls.objects.create(word=word, user=user)
