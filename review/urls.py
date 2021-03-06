from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.play, name='play'),
    url(r'^api/play$', views.PlayView.as_view(), name='play_api'),
    url(r'^api/guess/$', views.GuessView.as_view(), name='guess_api')
]
