# Generated by Django 4.2.7 on 2023-11-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex07', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
