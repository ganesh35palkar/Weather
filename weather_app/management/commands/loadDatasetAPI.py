import requests

from django.core.management.base import BaseCommand, CommandError
from weather_app.models import Country, WeatherData, YearMonth

class Command(BaseCommand):
    #python manage.py loadDataset countries=['UK','England','Scotland','Wales'] attributes=['Tmax', 'Tmin', 'Rainfall'] bucket_url='https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/'
    help = 'Load Datasets from S3'

    def add_arguments(self, parser):
        # Named (optional) arguments
        # Positional arguments are standalone name
        parser.add_argument('host_url')

        parser.add_argument('--countries',
                            action='store_true',
                            dest='countries',
                            default=['UK','England','Scotland','Wales'],
                            help='Provide country names')

        parser.add_argument('--attributes',
                            action='store_true',
                            dest='attributes',
                            default=['Tmax', 'Tmin', 'Rainfall'],
                            help='Provide weather attributes names')

        parser.add_argument('--bucket_url',
                            action='store_true',
                            dest='bucket_url',
                            default='https://s3.eu-west-2.amazonaws.com'
                                    '/interview-question-data/metoffice/',
                            help='Provide S3 bucket url')

    def handle(self, *args, **options):
        print options
        import urllib2
        import json
        for country in options.get('countries'):
            # country_obj = Country.objects.get_or_create(name=country)[0]
            for attribute in options.get('attributes'):
                response = urllib2.urlopen(options.get('bucket_url') +
                                           attribute+'-'+country+'.json')
                file_content = json.loads(response.read())
                self.stdout.write('Loading '+ country +' ' + attribute +
                                  ' data')
                for entry in file_content:
                    weather_data = {
                        "country": country,
                        "year": entry.get('year'),
                        "month": entry.get('month')
                    }
                    # if('year' not in entry):
                    # year_month_obj = YearMonth.objects.get_or_create(
                    #     year=entry.get('year'),
                    #     month=entry.get('month')
                    # )[0]
                    # import pdb; pdb.set_trace()
                    # weather_data_obj = WeatherData.objects.get_or_create(
                    #     country=country_obj,
                    #     year_month=year_month_obj)[0]

                    if (attribute == "Rainfall"):
                        weather_data["rain"] = entry.get('value')
                    if (attribute == "Tmax"):
                        weather_data["tmax"] = entry.get('value')
                    if (attribute == "Tmin"):
                        weather_data["tmin"] = entry.get('value')

                    # weather_data_obj.save()
                    r = requests.post(options.get("host_url") + "/weather/",
                                      json=weather_data)
                self.stdout.write(str(len(file_content)) + " Records inserted")
                self.stdout.write('Loading ' + country + ' ' + attribute +
                                  ' data Completed')

        self.stdout.write('Successfully Completed')
