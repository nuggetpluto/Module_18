from django.urls import path
from . import views

urlpatterns = [
    path('func_view/', views.func_view, name='func_view'),
    path('class_view/', views.ClassView.as_view(), name='class_view'),
]
