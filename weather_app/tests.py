from django.test import RequestFactory
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from weather_app import views


##########################################################################
# WEATHER DATA TEST CASE
##########################################################################


class WeatherCreteTests(APITestCase):
    """
    Test Cases for Weather Data related operations
    """

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_weather_data_get(self):
        """
        Test case for get weather data
        """
        url = '/weather/'
        factory = APIRequestFactory()
        view = views.WeatherListCreateAPIView.as_view()

        request = factory.get(url)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_weather_data_create(self):
        """
        Test case for create/update weather data
        """
        url = '/weather/'
        data = {
            "rain": 10.0,
            "year": 2018,
            "month": 1,
            "country": "uk"
        }
        factory = APIRequestFactory()
        view = views.WeatherListCreateAPIView.as_view()

        request = factory.post(url, data=data, format='json')
        response = view(request)
        self.assertEqual(response.status_code, 200)
