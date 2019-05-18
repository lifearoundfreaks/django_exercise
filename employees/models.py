from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    name_head = models.CharField(max_length=150, null=True, blank=True)
    parentId = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "Department"

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return self.id


class Position(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = "Position"

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return self.id


class Employees(models.Model):
    fullname = models.CharField(max_length=150)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    works_Data = models.DateField()
    salary = models.FloatField()

    class Meta:
        db_table = "Employees"

    def __str__(self):
        return '{}'.format(self.fullname)

    def get_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return self.id
