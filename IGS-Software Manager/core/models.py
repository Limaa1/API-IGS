from unittest.util import _MAX_LENGTH
from django.db import models
import django_tables2 as tables

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=50)

class Department(models.Model):
    departmentname = models.CharField(max_length=100, unique=True)


def __str__(self):
    return self.name

