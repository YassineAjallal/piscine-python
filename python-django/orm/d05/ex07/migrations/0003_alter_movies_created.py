# Generated by Django 4.2.7 on 2023-11-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex07', '0002_alter_movies_created_alter_movies_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]