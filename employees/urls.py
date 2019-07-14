from django.urls import path, include
from . import views
from .api import urls as api_urls

urlpatterns = [
    path('', views.employees),
    path('employees/<int:employee_id>/', views.employee),
    path('employees/add/', views.create_employee),
    path('employees/boss_reassign/', views.reassign_boss),
    path('employees/<int:employee_id>/delete/', views.delete_employee),
    path('employees/<int:employee_id>/edit/', views.edit_employee),
    path('search/', views.search),
    path('api', include(api_urls)),
]
