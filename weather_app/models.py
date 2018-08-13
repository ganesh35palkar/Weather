from __future__ import unicode_literals
import datetime


from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30)


class YearMonth(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.year and self.month:
            self.date = datetime.date(year=self.year, day=01, month=self.month)
            super(YearMonth, self).save(*args, **kwargs)


class WeatherData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year_month = models.ForeignKey(YearMonth, on_delete=models.CASCADE)
    rain = models.CharField(max_length=6, null=True, blank=True)
    tmin = models.CharField(max_length=6, null=True, blank=True)
    tmax = models.CharField(max_length=6, null=True, blank=True)
