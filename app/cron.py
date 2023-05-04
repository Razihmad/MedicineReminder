from .models import Patient
def my_cron_job():
    pat = Patient(name='Ra',phone='+919354715998',city='BLY',age='23',sex='Male')
    pat.save()
