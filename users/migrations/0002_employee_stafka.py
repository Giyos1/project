# Generated by Django 4.0.5 on 2022-06-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='stafka',
            field=models.IntegerField(choices=[(0.5, 0.5), (1, 1)], default=0.5),
        ),
    ]
