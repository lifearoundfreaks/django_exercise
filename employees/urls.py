from django.urls import path, include
from . import views
from .api import urls as api_urls

urlpatterns = [
    path('', views.employees),
    path('search/', views.search),
    path('api', include(api_urls)),
]
