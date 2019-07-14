from employees.models import Employee, Department, Position
from rest_framework import viewsets
from .pagination import EmployeePagination
from .serializers import (EmployeeSerializer,
                          DepartmentSerializer,
                          PositionSerializer,)
from rest_framework.permissions import IsAdminUser


class EmployeeRestView(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination
    permission_classes = (IsAdminUser,)


class DepartmentRestView(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PositionRestView(viewsets.ReadOnlyModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
