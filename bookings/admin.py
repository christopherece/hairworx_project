from django.contrib import admin

# Register your models here.
from .models import Booking, Employee, Service, Site

class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'name','stylist_name', 'email', 'phone',
        'location','date_chosen','time_chosen',
        'services'
    )
    search_fields = ('stylist_name', 'date_chosen','location')
    list_per_page = 25

class StylistAdmin(admin.ModelAdmin):
    list_display = (
        'location'
    )
    search_fields = ('stylist_name', 'date_chosen','location')
    list_per_page = 25


admin.site.register(Booking, BookingAdmin)
admin.site.register(Service)
admin.site.register(Site)
admin.site.register(Employee)







