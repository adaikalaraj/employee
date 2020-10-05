from django.forms import ModelForm
from staff.models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('employee_name', 'department')