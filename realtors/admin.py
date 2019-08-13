from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
     list_display=("id","email","name",'hire_date')
     search_fields=("name","id")
     list_display_links=("email","name")


admin.site.register(Realtor,RealtorAdmin)
