from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.AutoPrediction.as_view(), name='auto_predict'),
]

