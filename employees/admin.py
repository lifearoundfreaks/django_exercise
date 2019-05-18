from django.contrib import admin
from .models import Employees
from .models import Department
from .models import Position

admin.site.register(Department)
admin.site.register(Employees)
admin.site.register(Position)
