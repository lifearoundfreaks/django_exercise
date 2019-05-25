from django.urls import path, include
from . import views
from rest_framework import routers


rest_router = routers.DefaultRouter()
rest_router.register('_employees', views.EmployeeRestView)
rest_router.register('_positions', views.PositionRestView)
rest_router.register('_departments', views.DepartmentRestView)


urlpatterns = [
    path('', views.employees),
    path('api', include(rest_router.urls)),
]
