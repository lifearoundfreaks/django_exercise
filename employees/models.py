from django.db import models
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "Position"

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return self.id


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    position = models.ForeignKey(
        Position, on_delete=models.SET_NULL, null=True, blank=True)
    works_Data = models.DateField()
    salary = models.FloatField()

    class Meta:
        db_table = "Employee"

    def __str__(self):
        return '{}'.format(self.fullname)

    def get_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return self.id
