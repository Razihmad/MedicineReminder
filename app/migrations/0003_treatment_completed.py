# Generated by Django 4.2 on 2023-04-03 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_patient_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='completed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
