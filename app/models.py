from django.db import models

from multiselectfield import MultiSelectField
# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10,choices=(("Male","Male"),("Female","Female")))


class Treatment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    disease = models.CharField(max_length=1000)
    medicine = models.CharField(max_length=1000)
    dosage = models.CharField(max_length=1000)
    days = MultiSelectField(max_length=100,choices=(("Monday","Monday"),("Tuesday","Tuesday"),("Wednesday","Wednesday"),("Thursday","Thursday"),
                                     ("Friday","Friday"),("Saturday","Saturday"),("Sunday","Sunday")
                                     ))
    