from django.contrib import admin
from django import forms
from .models import Employee, Position


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['boss'].queryset = Employee.objects.filter(
            position=self.instance.boss_position)


class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position)
