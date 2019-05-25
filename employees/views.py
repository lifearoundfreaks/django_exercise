from django.http import HttpResponse
from django.shortcuts import render
from .models import Employees
from django.db.models import Q
from django.views.generic import View
from django.http import Http404, JsonResponse


class SortFullName(View):

    def get(self, request):
        obj_list = Employees.objects.order_by("fullname")
        content = {
            "obj_list": obj_list,
            "title": "List"
        }
        return render(request, "employees/index.html", content)


class SortPosition(View):

    def get(self, request):
        obj_list = Employees.objects.order_by("position")
        content = {
            "obj_list": obj_list,
            "title": "List"
        }
        return render(request, "employees/index.html", content)


class SortSalary(View):

    def get(self, request):
        obj_list = Employees.objects.order_by("salary")
        content = {
            "obj_list": obj_list,
            "title": "List"
        }
        return render(request, "employees/index.html", content)


class SortDepartment(View):

    def get(self, request):
        obj_list = Employees.objects.order_by("department")
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


def search_fullname(request):

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
