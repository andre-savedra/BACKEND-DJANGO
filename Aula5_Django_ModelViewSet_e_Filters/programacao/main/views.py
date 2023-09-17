from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


class PeopleAPIView(ModelViewSet):   
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'eyeColor', 'height', 'gender']

class PlanetAPIView(ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'climate', 'diameter']
           
class StarshipsAPIView(ModelViewSet):
    queryset = Starships.objects.all()
    serializer_class = StarshipsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'model', 'passengers']
    