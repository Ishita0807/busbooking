from django.contrib import admin
from app.models import bus

# Register your models here.

class busService(admin.ModelAdmin):
    list_display = ('user', 'username', 'bus_number','start','end','date')

admin.site.register(bus,busService)
