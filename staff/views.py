from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from staff.models import Department
from staff.forms import EmployeeForm


class DepartmentListView(ListView):

    model = Department


class DepartmentDetailView(DetailView):

    model = Department


class CreateEmployeeView(CreateView):
	
    template_name = 'staff/create_employee.html'
    form_class = EmployeeForm
    success_url = '/departments/'
