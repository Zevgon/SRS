import re

from .models import WordStats
from .models import Bucket

from django.shortcuts import render
from django.utils import timezone
from review.models import Word
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


def play(request):
    return render(request, 'play.html', {})


class PlayView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        words = [w.to_obj() for w in Word.objects.all()]
        return Response(words)


class GuessView(APIView):
    permission_classes = [AllowAny]

    def _handle_incorrect(self, word):
        word_stats = WordStats.objects.get(word=word)
        word_stats.last_reviewed = timezone.now()
        word_stats.bucket = Bucket.objects.first()
        word_stats.know_status -= 1 if word_stats.know_status > 0 else 0
        word_stats.save()
        return word_stats

    def _handle_correct(self, word):
        word_stats = WordStats.objects.get(word=word)
        word_stats.last_reviewed = timezone.now()
        word_stats.times_right += 1
        word_stats.know_status += 1
        try:
            new_bucket = Bucket.objects.get(id=word_stats.bucket.id + 1)
            word_stats.bucket = new_bucket
        except Bucket.DoesNotExist:
            pass
        word_stats.save()
        return word_stats

    def _is_correct(self, guess, translation):
        return bool(re.search(r'\b%s\b' % re.escape(guess),
                              translation,
                              flags=re.IGNORECASE))

    def post(self, request):
        data = request.data
        try:
            word = Word.objects.get(id=int(data['wordId']))
        except Word.DoesNotExist:
            return Response({
                'error': 'Can\'t find word with id %s' % data.id
            })

        if self._is_correct(data['english'], word.english):
            word_stats = self._handle_correct(word)
        else:
            word_stats = self._handle_incorrect(word)

        return Response({'knowStatus': word_stats.know_status})
