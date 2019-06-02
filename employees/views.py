from django.shortcuts import render
from .models import Employee


def employees(request):
    if request.method == 'GET':
        # If our request has id, we'll return a list of subordinates
        if 'id' in request.GET:
            index = request.GET['id']
            employees = Employee.objects.filter(
                boss__id=index)

            content = {
                "employees": employees,
            }

            return render(request, "employees/card_list.html", content)

        # Otherwise just display employee tree page
        else:
            employees = Employee.objects.filter(
                position__boss_position__isnull=True)

            content = {
                "employees": employees,
                "title": "Employee tree view"
            }
            return render(request, "employees/index.html", content)


def search(request):
    content = {
        "title": "Employee search page"
    }
    return render(request, "employees/search.html", content)
