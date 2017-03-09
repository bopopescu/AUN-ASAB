from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Venue(models.Model):
    title = models.CharField(max_length=150)
    availability = models.BooleanField(default=True)


class Reservation(models.Model):
    creator = models.ForeignKey(User,
                                related_name='reservations')
    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    venue = models.CharField(max_length=150)
    phone = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    venue = models.ForeignKey('Venue')
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')


class Holiday(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    description = models.TextField()




# Create your models here.
