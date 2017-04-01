from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
import arrow
class Venue(models.Model):
    title = models.CharField(max_length=150)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    creator = models.ForeignKey(User,
                                related_name='reservations_created')
    venue = models.ForeignKey(Venue, related_name='reservations')
    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=15)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='approved')

    def get_absolute_url(self):
        return reverse('reservation_detail',args=[self.pk])

    def clean(self):
        # Checks that reservations are not made in the past
        reservation_start_time = arrow.get(self.start_time)
        reservation_end_time = arrow.get(self.end_time)

        if reservation_start_time < arrow.utcnow():
            raise ValidationError('start time cannot be in the past')

        if reservation_start_time < arrow.utcnow():
            raise ValidationError('end time cannot be in the past')

        if reservation_end_time < reservation_start_time:
            raise ValidationError('end time cannot be less than start time')


class Holiday(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    description = models.TextField()




# Create your models here.
