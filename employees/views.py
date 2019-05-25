from django.shortcuts import render
from .models import Employee, Department, Position
from rest_framework import viewsets
from .serializers import EmployeeSerializer, DepartmentSerializer, PositionSerializer


def employees(request):

    obj_list = Employee.objects.all().order_by("last_name")

    content = {
        "employees": obj_list,
        "title": "All employees"
    }
    return render(request, "employees/index.html", content)


class EmployeeRestView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentRestView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PositionRestView(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
