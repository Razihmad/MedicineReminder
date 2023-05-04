from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name','city','age','sex']
    # readonly_fields = ['']


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ['patient','disease','medicine','dosage']
    readonly_fields = ['count']

    