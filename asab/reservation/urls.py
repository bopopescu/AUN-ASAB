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
    url(r'^reservation/dashboard/$', views.dashboard, name='my_dashbaord'),

     url(r'^logged_out/$', views.logged_out, name='logout_then_login'),
     url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/asab/logged_out/'}, name='logout', ),



#     Login and Logout urls
#     url(r'^login/$', 'allauth.account.views.LoginView', name='account_login'),
#     url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
#     url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
#     url(r'^register/$', views.register, name='register'),
#     url(r'^profile/$', views.dashboard, name='dashboard')

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)