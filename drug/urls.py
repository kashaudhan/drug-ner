from django.urls import path
from . import views

urlpatterns = [
    path('text-to-drug-detail/', views.post_text, name='text-to-drug-detail'),
]
