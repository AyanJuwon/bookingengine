# Generated by Django 3.2 on 2022-02-11 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_bookedlisting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookedlisting',
            old_name='booked_space',
            new_name='listing',
        ),
    ]
