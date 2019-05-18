from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path(r'', employees_list),
    path(r'sort=fullname', employees_sort_fullname),
    path(r'sort=position', employees_sort_position),
    path(r'sort=department', employees_sort_department),
    path(r'sort=salary', employees_sort_salary),
    path(r'<int:id>/', employees_detail)
]
