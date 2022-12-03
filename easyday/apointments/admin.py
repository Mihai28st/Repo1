from django.contrib import admin

from apointments.models import *

admin.site.register(Employee)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Client)