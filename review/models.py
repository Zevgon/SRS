from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Bucket(models.Model):
    number = models.IntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        return str(self.number)


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    def validate_key(cls, key, kwargs):
        if key not in kwargs:
            raise Exception('Must include %s' % key)

    @classmethod
    def add(cls, **kwargs):
        for key in ['language', 'english', 'foreign', 'user_id']:
            cls.validate_key(key, kwargs)
        try:
            l = Language.objects.get(name=kwargs['language'])
        except Language.DoesNotExist:
            raise Exception('We don\'t support that language yet')
        kwargs['language'] = l
        cls.objects.create(**kwargs)
