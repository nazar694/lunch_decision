from django.contrib.auth.models import User
from django.db import models

from restaurants.models import Restaurant



class Vote(models.Model):
    DAYS_OF_WEEK = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='votes')
    day = models.IntegerField(choices=DAYS_OF_WEEK, default=0)

    class Meta:
        unique_together = ['employee', 'day']

    def __str__(self):
        return f"{self.employee} voted for {self.restaurant}"
