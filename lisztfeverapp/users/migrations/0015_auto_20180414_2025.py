# Generated by Django 2.0.4 on 2018-04-14 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20180414_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followartist',
            name='status',
        ),
        migrations.AddField(
            model_name='followartist',
            name='classification',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='followartist',
            name='follow',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='followartist',
            name='source',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
