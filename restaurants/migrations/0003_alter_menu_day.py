# Generated by Django 4.2.20 on 2025-04-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_alter_menu_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='day',
            field=models.CharField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=20),
        ),
    ]
