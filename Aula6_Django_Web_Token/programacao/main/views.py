from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class PeopleAPIView(ModelViewSet):   
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'eyeColor', 'height', 'gender']
    permission_classes = (IsAuthenticated,)  

class PlanetAPIView(ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'climate', 'diameter']
    permission_classes = (IsAuthenticatedOrReadOnly,)  
           
class StarshipsAPIView(ModelViewSet):
    queryset = Starships.objects.all()
    serializer_class = StarshipsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'model', 'passengers']
    permission_classes = (IsAuthenticated,)  
    