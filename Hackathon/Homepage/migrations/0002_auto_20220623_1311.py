# Generated by Django 3.2.5 on 2022-06-23 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='JobDescription',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='verifiedjoblisting',
            name='JobDescription',
            field=models.TextField(max_length=1000),
        ),
    ]