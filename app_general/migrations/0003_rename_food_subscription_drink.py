# Generated by Django 4.2.5 on 2023-10-07 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0002_subscription_food'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='food',
            new_name='drink',
        ),
    ]