# Generated by Django 4.0.1 on 2022-03-27 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrument',
            name='prescore',
        ),
    ]
