# Generated by Django 4.2.4 on 2023-09-28 00:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_planet_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 28, 0, 46, 55, 622150, tzinfo=datetime.timezone.utc)),
        ),
    ]