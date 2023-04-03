from decouple import config
from twilio.rest import Client
from datetime import datetime
from app.models import *
account_sid = config('accountSid')
auth_token = config('authToken')
fromNumber = config('myNumber')
client = Client(account_sid,auth_token)
def run():
    dt = datetime.now()
    day = dt.strftime("%A")
    if(Treatment.objects.filter(days__contains=day,completed=False).exists()):
        currentReminders = Treatment.objects.filter(days__contains=day,completed=False)
        for currentReminder in currentReminders:
            phone = currentReminder.patient.phone
            medicine = currentReminder.medicine
            dosage = currentReminder.dosage
            message = client.messages.create(
            from_=fromNumber,
            to=phone,
            body=f'Friendly reminder that you have to take {medicine} of amount {dosage}.',
            )
        print("reminders sent successfully")