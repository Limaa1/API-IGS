from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import ListView
from .models import Employee, Department
from .serializers import EmployeesSerializer, DepartmentSerializer
from .tables import EmployeeTable
from django_tables2 import SingleTableView

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer


class EmployeesListView(SingleTableView):
    model = Employee
    table_class = EmployeeTable
    template_name = 'webpage/employee_list.html'


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


