from django.contrib import admin

# Register your models here.
from .models import Doctor,Patient,Appointment,PatientDischargeDetails,ContactForm

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(PatientDischargeDetails)
admin.site.register(ContactForm)