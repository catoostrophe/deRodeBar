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


# Links every date to a specific housemate to check whether that housemate eats on that day
class HousemateEats(models.Model):
    NUMBER_CHOICES = [
        (0, 0),  # not eating with house
        (1, 1),  # eating with house
        (2, 2),  # eating with house + a friend
        (3, 3)  # eating with house + 2 friends
    ]
    name = models.CharField(max_length=20)
    date = models.DateField()
    eetMee = models.IntegerField(default=0, choices=NUMBER_CHOICES)

    def __str__(self):
        date = self.date.strftime("%d/%m/%Y")
        name = self.name
        date_name = date + ', ' + name
        return date_name
