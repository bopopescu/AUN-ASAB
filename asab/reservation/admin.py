from django.contrib import admin
from .models import Reservation, Venue, Holiday

class VenueAdmin(admin.ModelAdmin):
    list_display = ('title', 'availability',)


admin.site.register(Venue, VenueAdmin)

class HolidayAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description',),

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('venue', 'created', 'updated',
                    'start_time', 'end_time',
                    'phone', 'status',)

    list_filter = ('status', 'created', 'creator',)
admin.site.register(Reservation, ReservationAdmin)


# admin.site.register(Holiday, HolidayAdmin)
# Register your models here.
