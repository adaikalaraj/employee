from django.db import models


class Employee(models.Model):
    employee_name = models.CharField(max_length=250)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    email = models.EmailField(max_length=250, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.employee_name


class Department(models.Model):
    department_name = models.CharField(max_length=250)
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True,
        related_name='departments')

    def __str__(self):
        return self.department_name
