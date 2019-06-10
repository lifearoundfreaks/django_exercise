from django.urls import path, include
from . import views
from .api import urls as api_urls

urlpatterns = [
    path('', views.employees),
    path('employees/<int:employee_id>/', views.employee),
    path('search/', views.search),
    path('api', include(api_urls)),
]
