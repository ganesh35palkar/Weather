from rest_framework import serializers

from weather.non_null_serializer import BaseSerializer
from weather_app.models import Country, YearMonth, WeatherData


class CountrySerializer(BaseSerializer):
    class Meta:
        model = Country
        # fields = ('name', 'id')
        read_only_fields = ('id')


class YearMonthSerializer(BaseSerializer):
    class Meta:
        model = YearMonth
        # fields = ('year', 'month', 'id')
        read_only_fields = ('id')


class WeatherDataCreateSerializer(BaseSerializer):
    class Meta:
        model = WeatherData
        fields = ('country', 'year_month', 'rain', 'tmin', 'tmax', 'id')
        read_only_fields = ('id')


class WeatherDataSerializer(BaseSerializer):
    country = serializers.SerializerMethodField('get_country_name')

    def get_country_name(self, obj):
        return obj.country.name

    year_month = serializers.SerializerMethodField('get_year_months')

    def get_year_months(self, obj):
        return obj.year_month.date.strftime('%b %Y')

    class Meta:
        model = WeatherData
        # fields = ('country', 'year_month', 'rain', 'tmin', 'tmax', 'id')
        read_only_fields = ('id')
        depth=2

class WeatherDataSerializerRain(BaseSerializer):
    country = serializers.SerializerMethodField('get_country_name')

    def get_country_name(self, obj):
        return obj.country.name

    year_month = serializers.SerializerMethodField('get_year_months')

    def get_year_months(self, obj):
        return obj.year_month.date.strftime('%b %Y')

    class Meta:
        model = WeatherData
        fields = ('country', 'year_month', 'rain', 'id')
        read_only_fields = ('id')
        depth = 2

class WeatherDataSerializerTmin(BaseSerializer):
    country = serializers.SerializerMethodField('get_country_name')

    def get_country_name(self, obj):
        return obj.country.name

    year_month = serializers.SerializerMethodField('get_year_months')

    def get_year_months(self, obj):
        return obj.year_month.date.strftime('%b %Y')

    class Meta:
        model = WeatherData
        fields = ('country', 'year_month', 'tmin','id')
        read_only_fields = ('id')
        depth = 2

class WeatherDataSerializerTmax(BaseSerializer):
    country = serializers.SerializerMethodField('get_country_name')

    def get_country_name(self, obj):
        return obj.country.name

    year_month = serializers.SerializerMethodField('get_year_months')

    def get_year_months(self, obj):
        return obj.year_month.date.strftime('%b %Y')

    class Meta:
        model = WeatherData
        fields = ('country', 'year_month', 'tmax', 'id')
        read_only_fields = ('id')
        depth = 2
