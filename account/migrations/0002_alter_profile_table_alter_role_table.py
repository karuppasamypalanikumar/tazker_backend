# Generated by Django 4.2.3 on 2023-07-30 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='profile',
            table='user_profiles',
        ),
        migrations.AlterModelTable(
            name='role',
            table='user_roles',
        ),
    ]
