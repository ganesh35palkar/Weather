from django.conf.urls import url

from weather_app import views


urlpatterns = [

    url(r'^weather/$',
        views.WeatherListCreateAPIView.as_view(),
        name='weather'),
]
