# Generated by Django 4.0.1 on 2022-04-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_rate_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
