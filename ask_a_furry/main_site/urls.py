from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('question/<int:id>', views.question),
    path('ask', views.ask),
    path('tag/<str:tag>', views.tag),
    path('settings', views.settings),
    path('register', views.register),
    path('login', views.login),
]
