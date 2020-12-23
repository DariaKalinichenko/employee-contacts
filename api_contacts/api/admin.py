from django.contrib import admin

from .models import Client, Employee, DateContact

admin.site.register(Client)

admin.site.register(Employee)

admin.site.register(DateContact)
