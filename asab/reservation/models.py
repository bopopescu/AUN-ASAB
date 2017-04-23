from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from datetime import date
import arrow

from asab import celery_app




class Facility(models.Model):
    title = models.CharField(max_length=150)
    availability = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"

class Venue(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='venues/%Y/%m/%d',
    blank=True)
    available = models.BooleanField(default=True)
    facilities = models.ManyToManyField(Facility, through='Ownership',)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=200, db_index=True)

    def get_absolute_url(self):
        return reverse('venue_detail', args=[self.pk])


    def __str__(self):
        return self.title


class Ownership(models.Model):
    facility = models.ForeignKey(Facility)
    venue = models.ForeignKey(Venue)





class Reservation(models.Model):
    creator = models.ForeignKey(User,
                                related_name='reservations_created')
    facility = models.ForeignKey(Facility, related_name='reservations')
    # venue = models.ForeignKey(Venue,null=True)
    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    )

    LEVEL_CHOICES = (
        ('Freshman', 'FRESHMAN'),
        ('Sophmore', 'SOPHMORE'),
        ('Junior', 'JUNIOR'),
        ('Senior', 'SENIOR')
    )


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='approved')
    accepted = models.BooleanField(default=True)
    reason = models.TextField(null=True, blank=True)
    level = models.CharField(max_length=25,
                             choices=LEVEL_CHOICES,
                             default='FRESHMAN')

    task_id = models.CharField(max_length=50, blank=True, editable=False)
    # time_range = arrow.get(end_time).replace(hour=-start_time.hour, minute=start_time.minute)

    class Meta:
        ordering = ('end_time',)

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

        if reservation_start_time > reservation_end_time.replace(hours=2):
            raise ValidationError('You cannot book a facility for more than 2 hours')

    def schedule_reminder(self):

        reseration_start_time = arrow.get(self.start_time)
        now = arrow.utcnow()

        reminder_time = arrow.get(self.start_time)

        from .tasks import send_reminder
        result = send_reminder.apply_async((self.pk,), eta=arrow.utcnow())

        return result.id

    def save(self, *args, **kwargs):

        # check if we have scheduled a reminder for thisreservation before
        if self.task_id:
            # revoke that task in the event that its time has changed
            celery_app.control.revoke(self.task_id)
        # Save the reservation with self.pk used in sheduling the next reminder
        super(Reservation, self).save(*args, **kwargs)

        # shedule a new tsk for this reservation
        self.task_id = self.schedule_reminder()

        #  save the reservation with new task_id
        super(Reservation, self).save(*args, **kwargs)






class Holiday(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    description = models.TextField()




# Create your models here.
