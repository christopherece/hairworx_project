from django.contrib import admin

# Register your models here.
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'phone',
        'location','date_chosen','time_chosen',
        'description'
    )

admin.site.register(Booking, BookingAdmin)



