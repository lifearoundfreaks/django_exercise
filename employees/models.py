from django.db import models
import datetime


class Position(models.Model):
    # For now, let's just put department name after position name
    # TODO: implement proper department model
    name = models.CharField(max_length=100)

    # Without any bonuses
    base_salary = models.IntegerField(default=0)

    # If left blank, it is assumed that this position has no positions above it
    boss_position = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)

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
    # Employee name fields
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    # Position should not be blank!
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    # datetime.date() when employee was hired
    hiring_date = models.DateField(default=datetime.date.today)

    # This plus position.base_salary defines final salary
    additional_salary = models.IntegerField(default=0)

    # Actual salary
    @property
    def salary(self):
        return self.position.base_salary + self.additional_salary

    class Meta:
        db_table = "Employee"

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)

    def get_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return self.id
