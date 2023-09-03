#importando a biblioteca de 'caminhos' do django
from django.urls import path
#importando as views que criamos da nossa api:
from .views import *


urlpatterns = [
    #estamos criando a rota/endpoint de acesso à API!
    path("people/", PeopleAPIView.as_view(), name='people'),
    path("people/<int:peopleId>", PeopleAPIView.as_view(), name='peopleParameter'),
    path("planets/", PlanetAPIView.as_view(), name='planets'),
    path("planets/<int:planetId>", PlanetAPIView.as_view(), name='planetsParameter'),
    path("starships/", StarshipsAPIView.as_view(), name='starships'),    
    path("starships/<int:starshipId>", StarshipsAPIView.as_view(), name='starshipsParameter'),
]