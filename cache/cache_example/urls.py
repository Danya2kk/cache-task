# cache_example/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('category/<int:cat_id>/', views.post_list_by_category, name='post_list_by_category'),
]
