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
    bucket = models.ForeignKey(Bucket, null=True)
    language = models.ForeignKey(Language)
    user = models.ForeignKey(User)
    english = models.CharField(max_length=100)
    foreign = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '%s: %s' % (self.english, self.foreign) + ' (%s)' % self.language # NOQA

    def to_obj(self):
        return {
            'english': self.english,
            'foreign': self.foreign,
            'pronunciation': self.pronunciation
        }
