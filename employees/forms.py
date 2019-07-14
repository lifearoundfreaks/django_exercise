from django import forms
from .models import Employee, get_appropriate_bosses


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        if hasattr(self.instance, 'position'):
            self.fields['boss'].queryset = get_appropriate_bosses(
                self.instance.position,
                self.instance.dept,)
        else:
            self.fields['boss'].widget = forms.HiddenInput()
