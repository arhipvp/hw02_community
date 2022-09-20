from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/', views.group_without_params),
    path('group/<params>/', views.group_posts_with_params)
]