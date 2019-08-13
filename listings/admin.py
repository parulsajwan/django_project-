from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published','list_date','realtors')
    list_display_links=('id','title')
    list_filter=('realtors',)
    search_fields=('title','description','address','state','zipcode')
    list_editable=('is_published',)
admin.site.register(Listing,ListingAdmin)
