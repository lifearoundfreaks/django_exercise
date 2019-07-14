from django.shortcuts import render, redirect
from .models import Employee, get_appropriate_bosses
from .utilities import PaginationSetter
from django.db.models import Q
from django.core.exceptions import FieldDoesNotExist
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from .forms import EmployeeForm


@staff_member_required(login_url='login')
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
                boss__isnull=True)

            context = {
                "employees": employees,
                "title": "Employee tree view",
                "title_id": "tree",
            }
            return render(request, "employees/index.html", context)


@staff_member_required(login_url='login')
def employee(request, employee_id):
    context = {
        "employee": Employee.objects.get(id=employee_id),
        "form": EmployeeForm,
    }

    if request.method == 'GET':
        return render(request, "employees/personal.html", context)

    if request.method == 'POST':
        instance = get_object_or_404(Employee, id=employee_id)
        form = EmployeeForm(
            request.POST, request.FILES, instance=instance)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request, 'employees/personal.html', context)


@staff_member_required(login_url='login')
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

        try:
            # Query by which to search a database. Use whitespaces for
            # multiple words
            query = request.GET.get('query')
            if not query:
                raise ValueError
        except ValueError:
            query = ""

        # First, let's get all objects
        employees = Employee.objects.all()

        # Now let's filter by each word in query if any
        for word in query.split():
            employees = employees.filter(
                Q(last_name__icontains=word) |
                Q(first_name__icontains=word) |
                Q(position__name__icontains=word) |
                Q(department__name__icontains=word))

        # How much are we left with?
        total_number = employees.count()

        # Sort by which Employee field?
        sort_by = request.GET.get('sort_by')
        try:
            Employee._meta.get_field(sort_by)
            employees = employees.order_by(sort_by)[
                (page - 1) * page_size:page * page_size]
        except (ValueError, TypeError, FieldDoesNotExist):
            # We'll sort by last name by default
            employees = employees.order_by('last_name')[
                (page - 1) * page_size:page * page_size]

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


@staff_member_required(login_url='login')
def create_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {
        "form": form,
    }
    return render(request, "employees/create.html", context)


@staff_member_required(login_url='login')
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    print(request.FILES)
    form = EmployeeForm(
        request.POST or None, request.FILES or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect(f"/employees/{employee_id}")
    context = {
        "employee": employee,
        "form": form,
    }
    return render(request, "employees/edit.html", context)


@staff_member_required(login_url='login')
def delete_employee(request, employee_id):
    e = get_object_or_404(Employee, id=employee_id)
    if request.method == "POST":
        e.delete()
        return redirect("/")
    context = {
        "employee": e,
    }
    return render(request, "employees/delete.html", context)


@staff_member_required(login_url='login')
def reassign_boss(request):
    if request.method == 'POST':
        if 'boss_id' in request.POST and 'sub_id' in request.POST:
            boss = Employee.objects.get(id=request.POST['boss_id'])
            sub = Employee.objects.get(id=request.POST['sub_id'])
            if boss in get_appropriate_bosses(sub.position, sub.dept):
                sub.boss = boss
                sub.save()
                return HttpResponse(f"Successfully reassigned.")
            else:
                return HttpResponse(f"Boss position was inappropriate.")
