from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


class PeopleAPIView(APIView):
    def delete(self, request, peopleId = ''):
        peopleFound = None
        try:
            #busca o usuario com o id
            peopleFound = People.objects.get(id=peopleId)
        except People.DoesNotExist:
            return Response(status=404,data="People not Found!")
                
        peopleFound.delete() #deleta o usuario com o id encontrado
        return Response(status=200, data="People successfully deleted!")
    
    def put(self, request, peopleId = ''):
        peopleFound = None

        try:
            #o people já existente no banco:
            peopleFound = People.objects.get(id=peopleId)
        except People.DoesNotExist:
            return Response(status=404,data="People not Found!")
        
        #o people com os dados novos
        peopleJson = request.data #coletando o json que veio do cliente
        #update
        peopleSerialized = PeopleSerializer(peopleFound, data=peopleJson)
        peopleSerialized.is_valid(raise_exception=True)
        peopleSerialized.save()
        return Response(status=200, data=peopleSerialized.data)
    
    def post(self, request):
        #recebe o json que veio do cliente
        peopleJson = request.data
        #converter json em python!
        peopleSerialized = PeopleSerializer(data=peopleJson)
        #verifica se conversão é válida!
        peopleSerialized.is_valid(raise_exception=True)
        #salva no banco de dados (insert into people ...)
        peopleSerialized.save()
        return Response(status=201, data=peopleSerialized.data)
    
    def get(self, request, peopleId = ''):

        if peopleId == '': #se estiver vazio, pega tudo!

            peopleFound = ''

            #se receber filtro de ambos:
            if 'height' in request.GET and 'eyeColor' in request.GET:
                peopleFound = People.objects.filter(height__gt=request.GET['height']) | People.objects.filter(eyeColor__contains=request.GET['eyeColor'])
                # peopleFound = People.objects.filter(height__gt=request.GET['height']).filter(eyeColor__contains=request.GET['eyeColor'])
            elif 'eyeColor' in request.GET:
                peopleFound = People.objects.filter(eyeColor__contains=request.GET['eyeColor'])
            elif 'height' in request.GET:
                peopleFound = People.objects.filter(height__gt=request.GET['height'])
            else:
                #primeiro vamos fazer um select all do banco:
                peopleFound = People.objects.all() #select *from people;
            #agora pegamos os dados em python e mandamos p/ json
            peopleSerialized = PeopleSerializer(peopleFound, many=True)
            #manda a resposta para quem chamou a API:
            #Response(data="ok")
            return Response(peopleSerialized.data)
        else: #coletando people do id solicitado!
            try:
                peopleFound = People.objects.get(id=peopleId)
                #select *from people where id = peopleId
                peopleSerialized = PeopleSerializer(peopleFound, many=False)
                return Response(peopleSerialized.data)            
            except People.DoesNotExist:
                return Response(status=404, data='People Not Found!')

class PlanetAPIView(APIView):
    def get(self, request, planetId =''):
        if planetId == '':
            #primeiro vamos fazer um select all do banco:
            planetFound = Planet.objects.all() #select *from Planet;
            #agora pegamos os dados em python e mandamos p/ json
            planetSerialized = PlanetSerializer(planetFound, many=True)
            #manda a resposta para quem chamou a API:
            return Response(planetSerialized.data)
        else: 
            try:
                planetFound = Planet.objects.get(id=planetId)
                planetSerialized = PlanetSerializer(planetFound, many=False)
                return Response(planetSerialized.data)            
            except Planet.DoesNotExist:
                return Response(status=404, data='Planet Not Found!')
            
    def delete(self, request, planetId = ''):
        planetFound = None
        try:
            #busca o usuario com o id
            planetFound = Planet.objects.get(id=planetId)
        except Planet.DoesNotExist:
            return Response(status=404,data="Planet not Found!")
                
        planetFound.delete() #deleta o Planet com o id encontrado
        return Response(status=200, data="Planet successfully deleted!")
    
    def put(self, request, planetId = ''):
       
        planetFound = None

        try:
            #o people já existente no banco:
            planetFound = Planet.objects.get(id=planetId)
        except Planet.DoesNotExist:
            return Response(status=404,data="Planet not Found!")
        
        #o people com os dados novos
        planetJson= request.data #coletando o json que veio do cliente
        #update
        planetSerialized = PlanetSerializer(planetFound, data=planetJson)
        planetSerialized.is_valid(raise_exception=True)
        planetSerialized.save()
        return Response(status=200, data=planetSerialized.data)
    
    def post(self, request):
        #recebe o json que veio do cliente
        planetJson = request.data
        #converter json em python!
        planetSerialized = PlanetSerializer(data=planetJson)
        #verifica se conversão é válida!
        planetSerialized.is_valid(raise_exception=True)
        #salva no banco de dados (insert into people ...)
        planetSerialized.save()
        return Response(status=201, data=planetSerialized.data)
        
        
class StarshipsAPIView(APIView):
    def get(self, request, starshipId = ''):
        if starshipId == '':
            #primeiro vamos fazer um select all do banco:
            starshipsFound = Starships.objects.all() #select *from Starships;
            #agora pegamos os dados em python e mandamos p/ json
            starshipsSerialized = StarshipsSerializer(starshipsFound, many=True)
            #manda a resposta para quem chamou a API:
            return Response(starshipsSerialized.data)
        else:
            try:
                starshipsFound = Starships.objects.get(id=starshipId)
                starshipsSerialized = StarshipsSerializer(starshipsFound, many=False)            
                return Response(starshipsSerialized.data)
            except Starships.DoesNotExist:
                return Response(status=404,  data='Starship Not Found!')

    def delete(self, request, starshipId = ''):
        starshipFound = None
        try:
            #busca o starship com o id
            starshipFound = Starships.objects.get(id=starshipId)
        except Starships.DoesNotExist:
            return Response(status=404,data="Starship not Found!")
                
        starshipFound.delete() #deleta o Planet com o id encontrado
        return Response(status=200, data="Starship successfully deleted!")
    
    def put(self, request, starshipId = ''):
        starshipFound = None

        try:
            #o starship já existente no banco:
            starshipFound = Starships.objects.get(id=starshipId)
        except Starships.DoesNotExist:
            return Response(status=404,data="Starship not Found!")
        
        #o people com os dados novos
        starshipJson= request.data #coletando o json que veio do cliente
        #update
        starshipSerialized = StarshipsSerializer(starshipFound, data=starshipJson)
        starshipSerialized.is_valid(raise_exception=True)
        starshipSerialized.save()
        return Response(status=200, data=starshipSerialized.data)
    
    def post(self, request):
        #recebe o json que veio do cliente
        starshipJson = request.data
        #converter json em python!
        starshipSerialized = StarshipsSerializer(data=starshipJson)
        #verifica se conversão é válida!
        starshipSerialized.is_valid(raise_exception=True)
        #salva no banco de dados (insert into people ...)
        starshipSerialized.save()
        return Response(status=201, data=starshipSerialized.data)