# Generated by Django 4.2.8 on 2023-12-15 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='nb_points',
            field=models.IntegerField(default=0),
        ),
    ]
