# Generated by Django 2.0.4 on 2018-04-13 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180413_0957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='trackartist',
            old_name='artist_id',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='trackartist',
            old_name='user_id',
            new_name='user',
        ),
    ]
