from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('process_money', views.process_money),
#     path('gold_tally', views.gold),
]