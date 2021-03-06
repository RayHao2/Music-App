# Generated by Django 4.0.1 on 2022-03-27 01:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='rate',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=datetime.datetime(2022, 3, 27, 1, 8, 33, 719026))),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('rates', models.IntegerField(default=0)),
                ('instrumentID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.instrument')),
            ],
        ),
    ]
