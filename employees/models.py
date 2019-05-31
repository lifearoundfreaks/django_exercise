from django.db import models
import datetime


class Position(models.Model):
    name = models.CharField(max_length=100)

    # Without any bonuses
    base_salary = models.IntegerField(default=0)

    # If left blank, it is assumed that this position has no positions above it
    boss_position = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)

    # How much workers are expected to be on this position. Note, that this is
    # the amount under each boss, meaning that the total amount would be
    # 'expected_workers * appropriate_bosses'
    expected_workers = models.IntegerField(default=1)

    class Meta:
        db_table = "Position"

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return self.id


class Department(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "Department"

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

    # The way departments work should be the following: employee cannot have a
    # boss from another department, but can still have a boss without one
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, blank=True, null=True)

    # datetime.date() when employee was hired
    hiring_date = models.DateField(default=datetime.date.today)

    # This plus position.base_salary defines final salary
    additional_salary = models.IntegerField(default=0)

    # Chosen person, should be the one holding a 'boss_position'
    boss = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)

    # Actual salary
    @property
    def salary(self):
        return self.position.base_salary + self.additional_salary

    # Property for employee filtering
    @property
    def dept(self):
        return self.department

    # Position which is above this person's one
    @property
    def boss_position(self):
        return self.position.boss_position

    class Meta:
        db_table = "Employee"

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)

    def get_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return self.id


def get_appropriate_bosses(position, dept=None):
    # TODO write a proper docstring

    # If an employee works in a department they cannot work under
    # someone from another department

    # Also, they may only work under an appropriate boss

    if dept:
        return Employee.objects.filter(
            models.Q(position=position.boss_position),
            models.Q(department__isnull=True) |
            models.Q(department=dept)
            )
    else:
        return Employee.objects.filter(
            models.Q(position=position.boss_position))
