from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import Station

longitude = 48.2903198
latitude = 25.9175176

user_location = Point(latitude, longitude, srid=4326)


class Home(generic.ListView):
    model = Station
    context_object_name = 'stations'
    queryset = Station.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:50]
    template_name = 'index.html'