from django.urls import path
from informMe_app import views

urlpatterns = [
    path('', views.posts_index, name='posts_index'),
    path('<int:pk>/', views.posts_detail, name="posts_detail")
]
