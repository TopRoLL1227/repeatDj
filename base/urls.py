from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
    path('<str:new_path>/', views.add_test, name='1')
]
