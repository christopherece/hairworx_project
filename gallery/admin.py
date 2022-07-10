from django.contrib import admin

# Register your models here.
from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'photo',
    )
    search_fields = ('photo', 'created_date')
    list_per_page = 25


admin.site.register(Gallery, GalleryAdmin)



