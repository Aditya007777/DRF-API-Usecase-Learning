from django.urls import path
from . import views

urlpatterns = [
    path('', views.students),
    path('sneha/', views.snehagod),
    
]
