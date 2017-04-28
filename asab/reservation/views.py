from __future__ import unicode_literals



from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect, redirect, HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy, reverse
from allauth.account.adapter import DefaultAccountAdapter
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.template import RequestContext
from .models import Reservation, Holiday, Facility, Venue
from .forms import ReservationCreateForm, ReservationUpdateForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
import arrow
from braces.views import LoginRequiredMixin


def index(request):
    section = "home"
    return render(request, "reservation/home.html" ,{"section": section})

def venue_list(request):
    venues = Venue.objects.filter(available=True)
    return render(request, 'reservation/venue_list.html', {'venues': venues})

def venue_detail(request, pk):
    venue = get_object_or_404(Venue, pk=pk)


    request.session['venue'] = venue.id

    return render(request, 'reservation/venue_detail.html', {'venue': venue})


class ReservationListView(ListView):
    model = Reservation

class ReservationDetailView(DetailView):
    model = Reservation

class ReservationDeleteView(DeleteView, LoginRequiredMixin):
    model = Reservation
    success_url = reverse_lazy('reservation_list')

# class ReservationUpdateView(UpdateView):
#     model = Reservation
#     fields = ['venue','start_time', 'end_time','phone',]

@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(creator=request.user, )

    return render(request, "reservation/my_reservations.html", {"reservations": reservations,})

@login_required
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
            selected_facility = reservation.facility

            if check_start_conflict(selected_facility, start, end):
                r_start_conflict = True

            if check_end_conflict(selected_facility, start, end):
                r_end_conflict = True

            if check_during_conflict(selected_facility, start, end):
                r_during_conflict = True

            if check_start_end_conflict(selected_facility, start, end):
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



def check_start_conflict(facility, start, end):
    start_conflict = Reservation.objects.filter(
                status='approved',
                facility__title=facility,
                start_time__gt=start, end_time__lt=end
                )
    if start_conflict:
        return True

def check_end_conflict(facility, start, end):
    end_conflict = Reservation.objects.filter(
                status='approved',
                facility__title=facility,
                start_time__gt=start, end_time__lt=end
                )
    if end_conflict:
        return True

def check_during_conflict(facility, start, end):
    during_conflict = Reservation.objects.filter(
                status='approved',
                facility__title=facility,
                start_time__lt=start, end_time__gt=end
            )
    if during_conflict:
        return True

def check_start_end_conflict(facility, start, end):
    start_end_conflict = Reservation.objects.filter(
                status='approved',
                facility__title=facility,
                start_time=start, end_time=end
            )
    if start_end_conflict:
        return True

@login_required
def new_reservation(request):
    conflict = False
    r_start_conflict = False
    r_end_conflict = False
    r_during_conflict = False
    r_start_end_conflict = False
    start_end_conflict = False
    qs = None


    qs = Venue.objects.get(id=request.session['venue']).facilities.all()


    if not qs:
        qs = None

    if request.method == 'POST':
        form = ReservationCreateForm(data=request.POST, options=[(choice.id, choice)for choice in qs])

        if form.is_valid():
            cd = form.cleaned_data
            start = cd['start_time']
            end = cd['end_time']
            phone = cd['phone']
            selected_facility = cd['facility']



            # start_conflict = Reservation.objects.filter(
            #     status='approved',
            #     facility__title=selected_facility,
            #     start_time__gt=start, start_time__lt=end
            #     )
            #
            # end_conflict = Reservation.objects.filter(
            #     status='approved',
            #     facility__title=selected_facility,
            #     end_time__gt=start, end_time__lt=end
            #     )
            #
            # during_conflict = Reservation.objects.filter(
            #     status='approved',
            #     facility__title=selected_facility,
            #     start_time__lt=start, end_time__gt=end
            # )
            #
            # start_end_conflict = Reservation.objects.filter(
            #     status='approved',
            #     facility__title=selected_facility,
            #     start_time=start, end_time=end
            # )
            #
            if check_start_conflict(selected_facility, start, end):
                r_start_conflict = True

            if check_end_conflict(selected_facility, start, end):
                r_end_conflict = True


            if check_during_conflict(selected_facility, start, end):
                r_during_conflict = True

            if check_start_end_conflict(selected_facility, start, end):
                r_start_end_conflict = True


            if (r_start_conflict or r_end_conflict or r_during_conflict or r_start_end_conflict):
                conflict = True


            if (start < arrow.utcnow() or end < arrow.utcnow()):
                return render(request, "reseration/reservation_past_conflict.html")

            if conflict:

                conflicting_reservations = Reservation.objects.filter(start_time__lte=start)
                return render(request, 'reservation/reservation_conflict.html', {'conflict':conflict,
                                                                                 'conflicting_reservations':conflicting_reservations})
            else:
                reservation = form.save(commit=False)
                reservation.creator = request.user
                reservation.start_time = start
                reservation.end_time = end
                reservation.phone = phone
                reservation.facility__title=selected_facility
                reservation.save()

                return redirect('reservation_detail', pk=reservation.pk)
    else:
        form = ReservationCreateForm(options=[(choice.id, choice)for choice in qs])
    return render(request, 'reservation/create_reservation.html', {'form': form,})
                                                                   # 'r_start_conflict': r_start_conflict,
                                                                   # 'r_end_conflict': r_end_conflict,
                                                                   # 'r_during_conflict': r_during_conflict,

# Registration views
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html',
                  {'user_form':user_form})


# ACCOUNT_ADAPTER = 'project.users.allauth.AccountAdapter'                                                                  # 'r_start_end_conflict': r_start_end_conflict})
# @login_required
# class AccountAdapter(DefaultAccountAdapter):
#
#   def get_login_redirect_url(self, request):
#       return '/reservation/account/dashboard.html'
#
#

@login_required
def dashboard(request):
    return render(request,
        'reservation/account/dashboard.html',)

def logged_out(request):
    return render(request,
                  'reservation/account/logged_out.html',)


# Create your views here.
