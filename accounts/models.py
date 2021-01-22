from django.db import models


class Housemate(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Cook(models.Model):
    user_objects = Housemate.objects.all()
    PEOPLE_CHOICES = []
    for user in user_objects:
        PEOPLE_CHOICES.append((user.name, user.name))
    date = models.DateField()
    amount = models.FloatField()
    kok = models.CharField(max_length=20, choices=PEOPLE_CHOICES)
    totalPeople = models.IntegerField()

    def __str__(self):
        return self.date.strftime("%d/%m/%Y")


class HousemateCook(models.Model):
    NUMBER_CHOICES = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3)
    ]
    name = models.CharField(max_length=20)
    date = models.DateField()
    eetMee = models.IntegerField(default=0, choices=NUMBER_CHOICES)

    def __str__(self):
        date = self.date.strftime("%d/%m/%Y")
        name = self.name
        date_name = date + ', ' + name
        return date_name
