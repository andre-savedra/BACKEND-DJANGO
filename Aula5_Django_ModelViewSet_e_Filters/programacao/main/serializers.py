from rest_framework import serializers
from .models import *

#vai converter o python dos models em json p/ a api
class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = People
        fields = '__all__'
        
class PlanetSerializer(serializers.ModelSerializer):
        class Meta:
            many = True
            model = Planet
            fields = '__all__'

class StarshipsSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Starships
        fields = '__all__' 
