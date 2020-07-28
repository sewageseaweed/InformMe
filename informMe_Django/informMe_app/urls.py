from django.urls import path
from informMe_app import views

urlpatterns = [
    path('', views.inform_me, name='Home'),
]
