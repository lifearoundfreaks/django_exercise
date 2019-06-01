from django.shortcuts import render
from .models import Employee, Department, Position
from rest_framework import viewsets
from .serializers import EmployeeSerializer, DepartmentSerializer
from .serializers import PositionSerializer


def employees(request):
    if request.method == 'GET':
        # If our request has id, we'll return a list of subordinates
        try:
            index = request.GET['id']
            employees = Employee.objects.filter(
                boss__id=index)

            content = {
                "employees": employees,
            }

            return render(request, "employees/card_list.html", content)

        # Otherwise just display employee tree page
        except KeyError:
            employees = Employee.objects.filter(
                position__boss_position__isnull=True)

            content = {
                "employees": employees,
                "title": "Employee tree view"
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
