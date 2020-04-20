from django.urls import path
from encode.views import base64view

app_name = 'encode'

urlpatterns = [
    path('base64/', base64view, name='base64'),
]