from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.categories, name='categories'),
    url(r'^question/(?P<category>\w+)', views.question, name='question'),
]