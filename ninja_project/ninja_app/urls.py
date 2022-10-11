from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('form', views.money),
    path('reset', views.reset),
]