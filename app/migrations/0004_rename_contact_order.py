# Generated by Django 3.2.4 on 2021-10-10 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_phone_number_contact_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='order',
        ),
    ]
