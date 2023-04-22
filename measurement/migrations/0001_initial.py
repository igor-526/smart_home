# Generated by Django 4.2 on 2023-04-22 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.CharField(max_length=50, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Датчик',
                'verbose_name_plural': 'Датчики',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField(verbose_name='Температура')),
                ('dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor', verbose_name='Датчик')),
            ],
            options={
                'verbose_name': 'Измерение',
                'verbose_name_plural': 'Измерения',
            },
        ),
    ]
