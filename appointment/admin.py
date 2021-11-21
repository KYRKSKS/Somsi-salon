from django.contrib import admin

# Register your models here.
from .models import AboutUs
from .models import Appointment

admin.site.register(AboutUs)
admin.site.register(Appointment)
