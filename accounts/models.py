from django.db import models


class Housemate(models.Model):
    name = models.CharField(max_length=20, default="", editable=False)

    def __str__(self):
        return self.name


class Cook(models.Model):
    date = models.DateField()
    amount = models.FloatField()
    kok = models.CharField(max_length=20)
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
    eetMee = models.IntegerField(default=0, choices=NUMBER_CHOICES)
    cook = models.ForeignKey(Cook, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
