from django.conf.urls import url
from django.conf import settings
from .views import ReservationDetailView, ReservationListView, my_reservations, ReservationDeleteView, \
    reservation_update, new_reservation, venue_list, venue_detail
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^reservations/$', ReservationListView.as_view(), name='reservation_list'),
    url(r'^my_reservations/$', my_reservations, name='my_reservations'),
    url(r'^reservation/(?P<pk>[0-9]+)/$', ReservationDetailView.as_view(), name='reservation_detail'),
    url(r'^reservation/new/$', views.new_reservation, name='new_reservation'),
    url(r'^reservation/(?P<pk>[0-9]+)/delete/$', ReservationDeleteView.as_view(), name='delete_reservation'),
    url(r'^reservation/(?P<pk>[0-9]+)/update/$',reservation_update, name='update_reservation'),
    url(r'^reservation/venues/$',venue_list, name='venue_list'),
    url(r'^venue/(?P<pk>[0-9]+)/$', venue_detail, name='venue_detail'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)