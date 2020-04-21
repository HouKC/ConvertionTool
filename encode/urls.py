from django.urls import path
from encode.views import base64_view, ascii_view

app_name = 'encode'

urlpatterns = [
    path('base64/', base64_view, name='base64'),
    path('base64/encode', base64_view, name='base64_encode'),
    path('base64/decode', base64_view, name='base64_decode'),

    path('ascii/', ascii_view, name='ascii'),
    path('ascii/encode', ascii_view, name='ascii_encode'),
    path('ascii/decode', ascii_view, name='ascii_decode'),
]