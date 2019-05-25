from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path(r'', employees_list),
    path(r'sort_fullname/', SortFullName.as_view()),
    path(r'sort_position/', SortPosition.as_view()),
    path(r'sort_salary/', SortSalary.as_view()),
    path(r'sort_department/', SortDepartment.as_view()),
    path(r'<int:id>/', employees_detail),
    path(r'search_fullname/$', search_fullname, name='search_fullname'),
]
