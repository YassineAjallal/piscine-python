# Generated by Django 4.2.7 on 2023-11-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='director',
            field=models.CharField(max_length=32),
        ),
    ]