from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect, redirect, HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.template import RequestContext
from .models import Reservation, Holiday, Venue
from .forms import ReservationCreateForm, ReservationUpdateForm
from django.contrib.auth.decorators import login_required
import arrow


def index(request):
    return render(request, "reservation/home.html")


class ReservationListView(ListView):
    model = Reservation

class ReservationDetailView(DetailView):
    model = Reservation

class ReservationDeleteView(DeleteView):
    model = Reservation
    success_url = reverse_lazy('list_reservations')

# class ReservationUpdateView(UpdateView):
#     model = Reservation
#     fields = ['venue','start_time', 'end_time','phone',]

@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(creator=request.user)

    return render(request, "reservation/my_reservations.html", {"reservations": reservations,})


def reservation_update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    r_start_conflict = False
    r_end_conflict = False
    r_start_end_conflict = False
    r_during_conflict = False
    conflict = False

    if request.method == 'POST':
        form = ReservationUpdateForm(request.POST, instance=reservation)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.creator = request.user
            start = reservation.start_time
            end = reservation.end_time
            phone = reservation.phone
            selected_venue = reservation.venue

            if check_start_conflict(selected_venue, start, end):
                r_start_conflict = True

            if check_end_conflict(selected_venue, start, end):
                r_end_conflict = True

            if check_during_conflict(selected_venue, start, end):
                r_during_conflict = True

            if check_start_end_conflict(selected_venue, start, end):
                r_start_end_conflict = True


            if (r_start_conflict or r_end_conflict or r_during_conflict or r_start_end_conflict):
                conflict = True

            if conflict:
                return render(request, "reservation/reservation_conflict.html",{'r_start_conflict': r_start_conflict,
                                                                   'r_end_conflict': r_end_conflict,
                                                                   'r_during_conflict': r_during_conflict,
                                                                   'r_start_end_conflict': r_start_end_conflict})
            else:
                reservation.save()

                return redirect('reservation_detail', pk=reservation.pk)
    else:
        form = ReservationUpdateForm(instance=reservation)
    return render(request, 'reservation/create_reservation.html', {'form': form,})



def check_start_conflict(venue, start, end):
    start_conflict = Reservation.objects.filter(
                status='approved',
                venue__title=venue,
                start_time__gt=start, end_time__lt=end
                )
    if start_conflict:
        return True

def check_end_conflict(venue, start, end):
    end_conflict = Reservation.objects.filter(
                status='approved',
                venue__title=venue,
                start_time__gt=start, end_time__lt=end
                )
    if end_conflict:
        return True

def check_during_conflict(venue, start, end):
    during_conflict = Reservation.objects.filter(
                status='approved',
                venue__title=venue,
                start_time__lt=start, end_time__gt=end
            )
    if during_conflict:
        return True

def check_start_end_conflict(venue, start, end):
    start_end_conflict = Reservation.objects.filter(
                status='approved',
                venue__title=venue,
                start_time=start, end_time=end
            )
    if start_end_conflict:
        return True


def new_reservation(request):
    conflict = False
    r_start_conflict = False
    r_end_conflict = False
    r_during_conflict = False
    r_start_end_conflict = False
    start_end_conflict = None
    if request.method == 'POST':
        form = ReservationCreateForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            start = cd['start_time']
            end = cd['end_time']
            phone = cd['phone']
            selected_venue = cd['venue']

            # start_conflict = Reservation.objects.filter(
            #     status='approved',
            #     venue__title=selected_venue,
            #     start_time__gt=start, end_time__lt=end
            #     )

            # end_conflict = Reservation.objects.filter(
            #     status='approved',
            #     venue__title=selected_venue,
            #     end_time__gt=start, end_time__lt=end
            #     )

            # during_conflict = Reservation.objects.filter(
            #     status='approved',
            #     venue__title=selected_venue,
            #     start_time__lt=start, end_time__gt=end
            # )

            # start_end_conflict = Reservation.objects.filter(
            #     status='approved',
            #     venue__title=selected_venue,
            #     start_time=start, end_time=end
            # )

            if check_start_conflict(selected_venue, start, end):
                r_start_conflict = True

            if check_end_conflict(selected_venue, start, end):
                r_end_conflict = True

            if check_during_conflict(selected_venue, start, end):
                r_during_conflict = True

            if check_start_end_conflict(selected_venue, start, end):
                r_start_end_conflict = True


            if (r_start_conflict or r_end_conflict or r_during_conflict or r_start_end_conflict):
                conflict = True

            if (start < arrow.utcnow() or end < arrow.utcnow()):
                return render(request, "reseration/reservation_past_conflict.html")

            if conflict:
                return render(request, 'reservation/reservation_conflict.html')
            else:
                reservation = form.save(commit=False)
                reservation.creator = request.user
                reservation.start_time = start
                reservation.end_time = end
                reservation.phone = phone
                reservation.venue__title=selected_venue
                reservation.save()

                return redirect('reservation_detail', pk=reservation.pk)
    else:
        form = ReservationCreateForm()
    return render(request, 'reservation/create_reservation.html', {'form': form,
                                                                   'r_start_conflict': r_start_conflict,
                                                                   'r_end_conflict': r_end_conflict,
                                                                   'r_during_conflict': r_during_conflict,
                                                                   'r_start_end_conflict': r_start_end_conflict})















# Create your views here.
