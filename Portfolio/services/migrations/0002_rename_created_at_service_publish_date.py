# Generated by Django 4.2.4 on 2023-09-04 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='created_at',
            new_name='publish_date',
        ),
    ]
