from django.shortcuts import render
from review.models import Word


def play(request):
    word = Word.objects.last()
    data = {
        'foreign': word.foreign,
        'pronunciation': word.pronunciation
    }
    return render(request, 'play.html', data)
