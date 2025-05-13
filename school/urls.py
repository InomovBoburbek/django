from django.urls import path
from .import views


urlpatterns = [
    path('', views.salom),
    path('info/', views.class_info)
]
