# Generated by Django 4.2.7 on 2023-11-18 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('title', models.CharField(max_length=64)),
                ('episode_nb', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('opening_crawl', models.TextField()),
                ('director', models.CharField(max_length=32)),
                ('producer', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
        ),
    ]
