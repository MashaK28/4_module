from django.urls import path
from .views import lesson_4_index


urlpatterns = [
    path('', lesson_4_index),
]