# Generated by Django 3.0.2 on 2020-03-14 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageApp', '0003_roominfo_curfee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roominfo',
            name='RoomPass',
        ),
    ]