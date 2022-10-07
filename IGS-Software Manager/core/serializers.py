from rest_framework import serializers
from .models import Employee, Department
from rest_framework.serializers import ValidationError
import re
import sqlite3
import django_tables2 as tables


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department']

    def validate_email(self, value):
        regex = "^[a-zA-Z0-9-_/.]+@[a-zA-Z0-9-/-]+\.[a-z]"
        if re.match(regex,value):
            return value
        raise ValidationError("Email is not valid")

    def validate_department(self, value):
        connection = sqlite3.connect('db.sqlite3', check_same_thread=False)
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM core_department")
        data=cursor.fetchall()
        data2 = ",".join(map(str,data))
        print (data2)
        if value not in data2:
            raise ValidationError("Department does not exist")
        return value
        
        

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'departmentname']


