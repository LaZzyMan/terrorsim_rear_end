# Generated by Django 2.0.4 on 2018-05-10 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rear_end_services', '0003_region_region_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='region_id',
            new_name='rid',
        ),
        migrations.RemoveField(
            model_name='country',
            name='region_name',
        ),
    ]