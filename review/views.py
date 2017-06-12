from django.shortcuts import render
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
