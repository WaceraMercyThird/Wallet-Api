# Generated by Django 4.0.6 on 2022-08-26 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_alter_loan_loan_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='reward',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]