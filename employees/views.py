from django.shortcuts import render
from .models import Employees
from django.db.models import Q


def employees_sort_fullname(request):

    obj_list = Employees.objects.all().order_by("fullname")

    content = {
        "obj_list": obj_list,
        "title": "List"
    }
    return render(request, "employees/index.html", content)


def employees_sort_position(request):
    obj_list = Employees.objects.all().order_by("position")

    content = {
        "obj_list": obj_list,
        "title": "List"
    }
    return render(request, "employees/index.html", content)


def employees_sort_department(request):
    obj_list = Employees.objects.all().order_by("department")

    content = {
        "obj_list": obj_list,
        "title": "List"
    }
    return render(request, "employees/index.html", content)


def employees_sort_salary(request):
    obj_list = Employees.objects.all().order_by("salary")

    content = {
        "obj_list": obj_list,
        "title": "List"
    }
    return render(request, "employees/index.html", content)


def employees_list(request):

    search = request.GET.get('search', '')

    if search:
        obj_list = Employees.objects.filter(Q(fullname__icontains=search))
    else:
        obj_list = Employees.objects.all().order_by("fullname")

    content = {
        "obj_list": obj_list,
        "title": "List"
    }
    return render(request, "employees/index.html", content)


def employees_detail(request, id=None):
    instance = Employees.objects.get(id=id)
    content = {
        "instance": instance,
        "title": "Detail"
    }
    return render(request, "employees/employees_details.html", content)
