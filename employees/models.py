from django.db import models
import datetime
from random import choice
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Position(models.Model):
    name = models.CharField(max_length=100)

    # Without any bonuses
    salary = models.IntegerField(default=0)

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
        return f'{self.name}'

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
        return f'{self.name}'

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return self.id


class Employee(models.Model):
    # Employee name fields
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    # Photo
    photo = models.ImageField(default="nophoto.png", blank=True)

    # Position should not be blank!
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    # The way departments work should be the following: employee cannot have a
    # boss from another department, but can still have a boss without one
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, blank=True, null=True)

    # datetime.date() when employee was hired
    hiring_date = models.DateField(default=datetime.date.today)

    # Should be based on position.salary
    salary = models.IntegerField(default=0)

    # Chosen person, should be the one holding a 'boss_position'
    boss = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True, blank=True)

    # Property for employee filtering
    @property
    def dept(self):
        return self.department

    # Position which is above this person's one
    @property
    def boss_position(self):
        return self.position.boss_position

    # Does this employee have subordinates?
    @property
    def has_subordinates(self):
        return len(Employee.objects.filter(boss__id=self.id)) > 0

    class Meta:
        db_table = "Employee"

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def get_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return self.id


def get_appropriate_bosses(position, dept=None, last_boss=None):
    """ Get a queryset of all employees who are of an appropriate position to
    be a boss to an employee with passed position

    :param position: position to which we want to find bosses
    :type position: 'models.Position'
    :param dept: optional department, boss can't be from another department
    :type dept: 'models.Department', optional
    :param last_boss: previous boss if any; we'll simply exclude him from query
    :type last_boss: 'models.Employee', optional
    :return: queryset with appropriate bosses
    :rtype: 'django.db.models.query.QuerySet'
    """

    # If an employee works in a department they cannot work under
    # someone from another department

    # Also, they may only work under an appropriate boss
    result = None

    # If an employee has a department exclude bosses with other departments
    if dept:
        result = Employee.objects.filter(
            models.Q(position=position.boss_position),
            models.Q(department__isnull=True) |
            models.Q(department=dept)
            )
    # Else just search normally
    else:
        result = Employee.objects.filter(
            models.Q(position=position.boss_position))

    # Excluding previous boss from queryset
    if last_boss:
        result = result.exclude(id=last_boss.id)

    return result


@receiver(pre_delete, sender=Employee)
def handlePreDelete(sender, **kwargs):
    """ Handling employee deletion event """
    # Getting employee instance
    boss = kwargs['instance']
    # Finding all subordinates
    subordinates = boss.employee_set.all()

    # For each subordinate
    for employee in subordinates:
        try:
            # Try to find appropriate new bosses
            appropriate = get_appropriate_bosses(
                    employee.position, employee.department, boss)
            # Choose a random one
            employee.boss = choice(appropriate)
        except IndexError:
            # In case there were none, nullify the field
            employee.boss = None
        # Don't forget to save the changes
        employee.save()
