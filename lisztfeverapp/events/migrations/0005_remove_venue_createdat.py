# Generated by Django 2.0.4 on 2018-04-16 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20180416_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='createdat',
        ),
    ]
