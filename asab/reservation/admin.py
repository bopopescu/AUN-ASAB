from django.contrib import admin
from .models import Reservation, Facility, Holiday, Venue, Ownership

# #
class OwnershipInline(admin.TabularInline):
    model = Ownership
    extra = 1

class VenueAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'photo','available',)
    inlines = [OwnershipInline,]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Venue, VenueAdmin)

class FacilityAdmin(admin.ModelAdmin):
    inlines = [OwnershipInline,]

admin.site.register(Facility, FacilityAdmin)

class HolidayAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description',),

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('facility', 'created', 'updated',
                    'start_time', 'end_time',
                    'phone', 'email', 'status',)

    list_filter = ('status', 'created', 'creator',)
admin.site.register(Reservation, ReservationAdmin)


# admin.site.register(Holiday, HolidayAdmin)
# Register your models here.
