
from django.contrib import admin

from django.urls import path

from .views import *

urlpatterns = [

    path('voting', main, name='voting'),

    path('vote/', vote, name='vote'),

    path('get-images/', get_images, name='get_images'),

    path('', top_images, name='top_images'),

]