# Generated by Django 3.2.4 on 2021-10-10 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_contact_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
    ]
