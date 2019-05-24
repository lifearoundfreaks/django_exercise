from django.shortcuts import render
from .models import Employee


def employees(request):

    obj_list = Employee.objects.all().order_by("last_name")

    content = {
        "obj_list": obj_list,
        "title": "All employees"
    }
    return render(request, "employees/index.html", content)
