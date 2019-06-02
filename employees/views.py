from django.shortcuts import render
from .models import Employee
from .utilities import PaginationSetter


def employees(request):
    if request.method == 'GET':
        # If our request has id, we'll return a list of subordinates
        if 'id' in request.GET:
            index = request.GET['id']
            employees = Employee.objects.filter(
                boss__id=index)

            context = {
                "employees": employees,
            }

            return render(request, "employees/card_list.html", context)

        # Otherwise just display employee tree page
        else:
            employees = Employee.objects.filter(
                position__boss_position__isnull=True)

            context = {
                "employees": employees,
                "title": "Employee tree view",
                "title_id": "tree",
            }
            return render(request, "employees/index.html", context)


def search(request):
    if request.method == 'GET':
        try:
            # Current page parameter. 1 by default
            page = max(int(request.GET.get('page')), 1)

        except (ValueError, TypeError):
            page = 1

        try:
            # Page size parameter. 10 by default
            page_size = max(int(request.GET.get('page_size')), 1)

        except (ValueError, TypeError):
            page_size = 10

        employees = Employee.objects.all()

        # Sort by which Employee field?
        sort_by = request.GET.get('sort_by')
        if sort_by and hasattr(Employee, sort_by):
            employees = employees.order_by(sort_by)[
                (page - 1) * page_size:page * page_size]
        else:
            # We'll sort by last name by default
            employees = employees.order_by('last_name')[
                (page - 1) * page_size:page * page_size]

        total_number = Employee.objects.all().count()

        # Different logic if this view was called by ajax
        if request.GET.get('ajax'):
            context = {
                "employees": employees,

                # Pagination setter sets html pagination layout
                "pagination": PaginationSetter(
                    (total_number // page_size) + 1, page
                ) if total_number > page_size else "",
            }
            return render(request, "employees/search_results.html", context)

        # Else render normally
        else:
            context = {
                "employees": employees,

                # Pagination setter sets html pagination layout
                "pagination": PaginationSetter(
                    (total_number // page_size) + 1, page
                ) if total_number > page_size else "",

                "title": "Employee search page",
                "title_id": "adv_search",
            }
            return render(request, "employees/search.html", context)
