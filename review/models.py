from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db import transaction
from utils.word_utils import get_words
from autoslug import AutoSlugField


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
    bucket = models.ForeignKey(Bucket, default=1)
    language = models.ForeignKey(Language)
    user = models.ForeignKey(User)
    english = models.CharField(max_length=100)
    foreign = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=200, null=True)
    last_reviewed = models.DateTimeField(null=True)
    times_right = models.IntegerField(default=0)
    know_status = models.IntegerField(default=0)

    def __str__(self):
        return '%s: %s' % (self.english, self.foreign) + ' (%s)' % self.language # NOQA

    def to_obj(self):
        return {
            'english': self.english,
            'foreign': self.foreign,
            'pronunciation': self.pronunciation
        }

    @classmethod
    def validate_keys(cls, keys, kwargs):
        for key in keys:
            if key not in kwargs:
                raise Exception('Must include %s' % key)

    @classmethod
    def add(cls, **kwargs):
        cls.validate_keys(
            ['language', 'english', 'foreign', 'user_id'], kwargs)
        if type(kwargs['language']) in [str, unicode]:
            try:
                l = Language.objects.get(title=kwargs['language'])
            except Language.DoesNotExist:
                raise Exception('We don\'t support that language yet')
            kwargs['language'] = l
        cls.objects.create(**kwargs)

    @classmethod
    @transaction.atomic
    def bulk_add(cls, words, user_id, language):
        word_kwargs = {}
        word_kwargs['user_id'] = user_id
        try:
            language_obj = Language.objects.get(title=language)
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
    def set_up_user_with_words(cls, user, language):
        words = get_words(language)
