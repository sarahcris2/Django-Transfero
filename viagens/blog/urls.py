from django.urls import path
from . import views
urlpatterns = [
    path('', views.artigos, name='blog'),
]