from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


class PeopleAPIView(APIView):
    def get(self, request):
        peopleFound = People.objects.all() #select *from people;
        serializer = PeopleSerializer(peopleFound, many=True)
        return Response(serializer.data)
    