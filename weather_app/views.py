import json
import requests

import datetime
from rest_framework.generics import (
    ListCreateAPIView,
)
from rest_framework.response import Response
from rest_framework import status

from weather_app.models import Country, WeatherData, YearMonth

from weather_app.serializers import (
    CountrySerializer,
    WeatherDataSerializer,
    YearMonthSerializer,
    WeatherDataSerializerRain,
    WeatherDataSerializerTmax,
    WeatherDataSerializerTmin,
    WeatherDataCreateSerializer
)

##############################################################################
# Weather Data API
##############################################################################
class WeatherListCreateAPIView(ListCreateAPIView):
    """
    Method Supported: GET POST
    Descriptions:
        API is consumed by User of App.
        Required User Login
        API is used to add new address to system or retrieve existing address from system
    Compulsory Fields: address_type
    Filtering Query Params: start_date, end_date, type, location
    """

    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    my_filter_fields = ('start_date', 'end_date', 'type', 'location',)

    def get_kwargs_for_filtering(self):
        """
        This is a self defined method for search.
        It searches on the basic of Address.
        It displays all the Address with search
        filter.
        """
        filtering_kwargs = {}
        for field in self.my_filter_fields:
            """
            iterate over the filter fields
            get the value of a field from request query parameter
            """
            field_value = self.request.query_params.get(field)
            if field_value:
                filtering_kwargs[field] = field_value
        return filtering_kwargs

    def get(self, request, format=None):
        filtering_args={}
        filtering_kwargs = self.get_kwargs_for_filtering()
        if(filtering_kwargs.get('start_date') and filtering_kwargs.get(
                'end_date')):
            start_date=datetime.datetime.strptime(
                filtering_kwargs.get('start_date'), "%Y-%m-%d").date()
            end_date=datetime.datetime.strptime(
                filtering_kwargs.get('end_date'), "%Y-%m-%d").date()

            filtering_args['year_month__in'] = YearMonth.objects.filter(
                date__range=[start_date, end_date]
            ).values_list('id', flat=True)
        if (filtering_kwargs.get('location')):
            filtering_args['country__in'] = Country.objects.filter(
                name__iexact=filtering_kwargs.get('location')
            ).values_list('id', flat=True)

        queryset = WeatherData.objects.filter(**filtering_args)
        if (filtering_kwargs.get('type')=="rain"):
            serializer = WeatherDataSerializerRain(queryset, many=True)
        elif (filtering_kwargs.get('type')=="tmin"):
            serializer = WeatherDataSerializerTmin(queryset, many=True)
        elif (filtering_kwargs.get('type')=="tmax"):
            serializer = WeatherDataSerializerTmax(queryset, many=True)
        else:
            serializer = WeatherDataSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        """
        This method checks whether the request is coming from the User.
        It is used to add new Address to system.
        """

        weather_data = request.data
        country_obj = Country.objects.get_or_create(
            name__iexact=weather_data.get('country'))[0]
        weather_data['country'] = country_obj.id

        year_month_obj = YearMonth.objects.get_or_create(
            year=weather_data.get('year'),
            month=weather_data.get('month')
        )[0]
        del weather_data['year']
        del weather_data['month']

        weather_data['year_month'] = year_month_obj.id

        weather_data_obj = WeatherData.objects.get_or_create(
            country=country_obj,
            year_month=year_month_obj)[0]

        serializer = WeatherDataCreateSerializer(weather_data_obj,
                                       data=weather_data,
                                       partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
