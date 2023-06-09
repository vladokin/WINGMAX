# Generated by Django 4.2 on 2023-04-22 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='status',
            field=models.IntegerField(choices=[(1, 'Planned'), (2, 'Taking off'), (3, 'On route'), (4, 'Landing'), (5, 'Completed'), (6, 'Canceled'), (7, 'Maxed out')], default=1),
        ),
    ]
