from django.contrib import admin

# Register your models here.
from .models import Booking, Service

class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'name','stylist_name', 'email', 'phone',
        'location','date_chosen','time_chosen',
        'services'
    )

admin.site.register(Booking, BookingAdmin)
admin.site.register(Service)




