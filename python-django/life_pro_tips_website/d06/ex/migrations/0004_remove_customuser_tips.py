# Generated by Django 4.2.8 on 2023-12-16 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0003_alter_tip_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='tips',
        ),
    ]
