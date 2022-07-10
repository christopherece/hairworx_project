from django.contrib import admin

# Register your models here.
from .models import Booking, Service

class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'stylist_name','name', 'email', 'phone',
        'location','date_chosen','time_chosen',
        'services'
    )

admin.site.register(Booking, BookingAdmin)
admin.site.register(Service)




