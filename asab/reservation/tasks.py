from __future__ import absolute_import


from celery import shared_task
from celery import Celery
from django.core.mail import send_mail


import arrow

from .models import Reservation

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def send_reminder(reservation_id):
    """
     Sends an e-mail notofication when a new reservation is created
    """
    try:
        reservation = Reservation.objects.get(pk=reservation_id)
    except reservation.DoesNotExist:
        return None
    facility = reservation.facility
    start = arrow.get(reservation.start_time)
    end = arrow.get(reservation.end_time)

    subject = 'Reservation notification'
    message = "Hello \n\nYou have successfully booked {} from {} to {}".format(facility,
                                                                                 start, end)

    mail_sent = send_mail(subject, message, 'asab.aun@gmail.com',
                          [reservation.email, 'asab.aun@gmail.com'], fail_silently=False)
    return mail_sent