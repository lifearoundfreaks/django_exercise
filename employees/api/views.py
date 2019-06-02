from employees.models import Employee, Department, Position
from rest_framework import viewsets
from .pagination import EmployeePagination
from .serializers import (EmployeeSerializer,
                          DepartmentSerializer,
                          PositionSerializer,)


class EmployeeRestView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination


class DepartmentRestView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PositionRestView(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
