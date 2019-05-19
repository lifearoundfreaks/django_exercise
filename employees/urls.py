from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path(r'', employees_list),
    path(r'<int:id>/', employees_details)
]
