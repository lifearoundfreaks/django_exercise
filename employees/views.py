from django.shortcuts import render
from .models import Employee


def employees_list(request):

    obj_list = Employee.objects.all().order_by("last_name")

    content = {
        "obj_list": obj_list,
        "title": "List"
    }
    return render(request, "employees/index.html", content)


def employees_details(request, id=None):
    instance = Employee.objects.get(id=id)
    content = {
        "instance": instance,
        "title": "Detail"
    }
    return render(request, "employees/employees_details.html", content)
