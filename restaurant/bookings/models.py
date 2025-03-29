from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Table(models.Model):
    TABLE_TYPES = (
        ('2', '2-person'),
        ('4', '4-person'),
        ('6', '6-person'),
        ('8', '8-person'),
    )
    number = models.IntegerField(unique=True)
    capacity = models.CharField(max_length=1, choices=TABLE_TYPES)
    location = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.number} ({self.get_capacity_display()})"

class Booking(models.Model):
    TIME_SLOTS = [
        ('11:00', '11:00 AM'),
        ('12:00', '12:00 PM'),
        ('13:00', '1:00 PM'),
        ('14:00', '2:00 PM'),
        ('18:00', '6:00 PM'),
        ('19:00', '7:00 PM'),
        ('20:00', '8:00 PM'),
        ('21:00', '9:00 PM'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_SLOTS)
    guests = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)]
    )
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_cancelled = models.BooleanField(default=False)  

    class Meta:
        unique_together = ('table', 'date', 'time')
        ordering = ['date', 'time']

    def __str__(self):
        return f"Booking #{self.id} - {self.user.username} on {self.date} at {self.time}"     