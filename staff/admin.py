from django.contrib import admin
from staff.models import Employee, Department
from rangefilter.filter import DateRangeFilter


class EmployeeInline(admin.TabularInline):
    model = Employee


class DepartmentAdmin(admin.ModelAdmin):
   inlines = [EmployeeInline,]


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_filter = (
        ('department', admin.RelatedOnlyFieldListFilter),
        ('date_of_birth', DateRangeFilter),
    )


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)