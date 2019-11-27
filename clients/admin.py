from django.contrib import admin
from .models import Client
# Register your models here.

class AdminClient(admin.ModelAdmin):
    list_display = ('site_name', 'client_name', 'phone', 'date')
    list_filter = ('date', 'client_name')
admin.site.register(Client, AdminClient)