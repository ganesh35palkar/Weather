# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rain', models.CharField(max_length=6, null=True, blank=True)),
                ('tmin', models.CharField(max_length=6, null=True, blank=True)),
                ('tmax', models.CharField(max_length=6, null=True, blank=True)),
                ('country', models.ForeignKey(to='weather_app.Country')),
            ],
        ),
        migrations.CreateModel(
            name='YearMonth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='year_month',
            field=models.ForeignKey(to='weather_app.YearMonth'),
        ),
    ]
