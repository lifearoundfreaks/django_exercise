from rest_framework import serializers
from .models import Employee, Position, Department


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = (
            'id',
            'url',
            'name',
            'base_salary',
            'boss_position',
            )


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id',
            'url',
            'name',
            )


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    position, department = PositionSerializer(), DepartmentSerializer()

    class Meta:
        model = Employee
        fields = (
            'id',
            'url',
            'first_name',
            'last_name',
            'position',
            'department',
            'hiring_date',
            'salary',
            'boss',
            )