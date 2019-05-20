from django.contrib import admin
from django import forms
from django.db.models import Q
from .models import Employee, Position, Department


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        # If an employee works in a department they cannot work under
        # someone from another department

        # Also, they may only work under an appropriate boss

        if hasattr(self.instance, 'position') and self.instance.dept:
            self.fields['boss'].queryset = Employee.objects.filter(
                Q(position=self.instance.boss_position),
                Q(department__isnull=True) | Q(department=self.instance.dept)
                )
        elif hasattr(self.instance, 'position') and not self.instance.dept:
            self.fields['boss'].queryset = Employee.objects.filter(
                Q(position=self.instance.boss_position))
        else:
            self.fields['boss'].widget = forms.HiddenInput()


class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position)
admin.site.register(Department)
