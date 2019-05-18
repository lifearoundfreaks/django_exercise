from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', employees_list),
    path(r'<int:id>/', employees_detail)
]