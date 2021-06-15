# Generated by Django 3.2.2 on 2021-06-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='POI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poi_info', models.TextField(blank=True, default='', null=True, verbose_name='Информация')),
            ],
            options={
                'verbose_name': 'Содержимое POI',
                'verbose_name_plural': 'Содержимое POI',
            },
        ),
    ]
