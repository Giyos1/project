# Generated by Django 4.0.5 on 2022-06-20 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_employee_stafka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='stafka',
            field=models.FloatField(choices=[(0.5, 0.5), (1, 1)], default=0.5),
        ),
    ]
