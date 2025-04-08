from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    DAYS_OF_WEEK = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    day = models.IntegerField(choices=DAYS_OF_WEEK, default=0)
    menu = models.TextField(max_length=150)

    class Meta:
        unique_together = ['restaurant', 'day']

    def __str__(self):
        return f"{self.restaurant.name}"
