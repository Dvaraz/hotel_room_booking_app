# Generated by Django 4.2.6 on 2023-10-29 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_remove_room_places_1_to_32_room_places_1_to_32'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='room',
            name='price_gte_0',
        ),
        migrations.AddConstraint(
            model_name='room',
            constraint=models.CheckConstraint(check=models.Q(('price__gte', 1)), name='price_gte_0'),
        ),
    ]
