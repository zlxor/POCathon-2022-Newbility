# Generated by Django 4.0.5 on 2022-06-17 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='documents',
            new_name='Documents',
        ),
    ]