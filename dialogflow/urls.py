from django.urls import path
from . import views

app_name = 'dialogflow'

urlpatterns = [
    path('', views.index, name='index'),
    path('fulfillment/', views.fulfillment, name='fulfillment'),
]
