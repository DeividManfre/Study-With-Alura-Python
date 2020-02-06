from django.urls import path
from .view import index, contact

urlpatterns = [
    path('', index),
    path('contact', contact),
]
