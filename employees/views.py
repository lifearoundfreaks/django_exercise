from django.shortcuts import render, redirect
from .models import Employee, get_appropriate_bosses
from .utilities import PaginationSetter
from django.db.models import Q
from django.core.exceptions import FieldDoesNotExist
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from .forms import EmployeeForm
from .decorators import user_access_error


@user_access_error
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


@user_access_error
@staff_member_required(login_url='login')
def employee(request, employee_id):
    context = {
        "employee": Employee.objects.get(id=employee_id),
        "form": EmployeeForm,
    }

    # Render appropriate employee's personal page
    return render(request, "employees/personal.html", context)


@user_access_error
@staff_member_required(login_url='login')
def search(request):
    if request.method == 'GET':
        # Current page parameter. 1 by default
        page = int(request.GET.get('page') or 1)

        # Page size parameter. 10 by default
        page_size = int(request.GET.get('page_size') or 10)

        # Search query. Empty string by default
        query = request.GET.get('query') or ""

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

        # Branching logic if this view was called by ajax
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
                "title_id": "adv-search",
            }
            return render(request, "employees/search.html", context)


@user_access_error
@staff_member_required(login_url='login')
def create_employee(request):
    # Form with employee data or no data
    form = EmployeeForm(request.POST or None)
    # If form is correctly filled
    if form.is_valid():
        # Save employee
        form.save()
        # Redirect to the main page
        return redirect("/")

    context = {
        "form": form,
        "title": "Employee creation",
        "title_id": "add-employee",
    }

    # Else, render template the same form
    return render(request, "employees/create.html", context)


@user_access_error
@staff_member_required(login_url='login')
def edit_employee(request, employee_id):
    # Get employee
    employee = get_object_or_404(Employee, id=employee_id)
    # Get employee form (with filled in fields)
    form = EmployeeForm(
        request.POST or None, request.FILES or None, instance=employee)

    # When form data was valid
    if form.is_valid():
        # Save employee
        form.save()
        # Redirect to their page
        return redirect(f"/employees/{employee_id}")

    context = {
        "employee": employee,
        "form": form,
        "title": "Updating employee",
    }

    # If not, render edit template
    return render(request, "employees/edit.html", context)


@user_access_error
@staff_member_required(login_url='login')
def delete_employee(request, employee_id):
    # Get employee
    e = get_object_or_404(Employee, id=employee_id)
    # POST means that user confirmed deletion
    if request.method == "POST":
        # Delete user
        e.delete()
        # Redirect to the main page
        return redirect("/")

    context = {
        "employee": e,
        "title": "Employee deletion",
    }

    # While not POST, ask for user confirmation via this template
    return render(request, "employees/delete.html", context)


@staff_member_required(login_url='login')
def reassign_boss(request):
    if request.method == 'POST':
        # If it's a proper request
        if 'boss_id' in request.POST and 'sub_id' in request.POST:
            # Find a boss
            boss = Employee.objects.get(id=request.POST['boss_id'])
            # Find a subordinate
            sub = Employee.objects.get(id=request.POST['sub_id'])
            # If boss is in appropriate position to subordinate
            if boss in get_appropriate_bosses(sub.position, sub.dept):
                # Make him subordinate's boss
                sub.boss = boss
                # Save subordinate
                sub.save()
                # And report that operation was successful
                return HttpResponse(f"Successfully reassigned.")
            else:
                # Else report failure
                return HttpResponse(f"Boss position was inappropriate.")
