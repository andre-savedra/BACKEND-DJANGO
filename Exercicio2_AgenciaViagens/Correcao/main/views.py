
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from rest_framework.response import Response
from datetime import datetime, timedelta

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .customFilters import *
from django.db.models import Avg

from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated

def strToDate(strDate):
    return datetime.strptime(strDate, '%Y-%m-%d').date()

class ScoreAverageView(APIView):
    def get(self, request, tripId = ''):
        if tripId == '': return Response(status=400,data='Missing required parameter tripId!')
        try:
            tripFound = Trip.objects.get(id=tripId)
            serializedTrip = TripSerializer(tripFound, many=False)
            average = Booking.objects.filter(tripFK=tripId).aggregate(Avg('score'))
            if average is not None: return Response(status=200, data={'average': average['score__avg'], 'trip': serializedTrip.data})            
            else: return Response(status=404, data='Was not possible to calculate average of trip with id: ' + tripId)
        except Trip.DoesNotExist:
            return Response(status=404,data='Trip with id: ' + tripId + ' was not found!')

#creating custom model viewset allowing multiple registers
class CustomModelViewSet(ModelViewSet):
    def create(self, request, *args, **kwargs):
       mySerializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
       mySerializer.is_valid(raise_exception=True)
       self.perform_create(mySerializer) 
       headers = self.get_success_headers(mySerializer.data)
       return Response(mySerializer.data, status=201, headers=headers)


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = CategoryFilter
    ordering_fields = '__all__'
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

class TripView(ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = TripFilter
    ordering_fields = '__all__'
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class ImageView(CustomModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class CustomUserView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = CustomUserFilter
    ordering_fields = '__all__'


class BookingView(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = BookingFilter
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = None
        if user.is_superuser:
            queryset = Booking.objects.all()
        else:
            #o usuario que solicitou a API tem que ser o mesmo usuario que fez a reserva deste pagamento
            queryset = Booking.objects.filter(customUserFK__user__username=user.username)
        return queryset    

#startDate = 01-01-2023
#endDate = 10-01-2023
#['01-01-2023', '02-01-2023', '03-01-2023'... '10-01-2023'  ]
#CHECAR DISPONIBILIDADE --> OK
#SALVAR RESERVA --> OK
#ATUALIZAR TABELA DE DISPONIBILIDADE COM O ID DA RESERVA -->

    def create(self, request, *args, **kwargs):
        data = request.data
        dayList = []
        availabilities = []
        currentDate = strToDate(data['startDate'])
        while currentDate <= strToDate(data['endDate']):
            dayList.append(currentDate)
            currentDate += timedelta(days=1)
        
        #checking all availabilities:
        for dateChosen in dayList:
            availability = Availability.objects.filter(tripFK=data['tripFK']).filter(date=dateChosen).filter(bookingFK=None).first()
            if availability is None:
                return Response(status=409,data='Period between ' + data['startDate'] + ' and ' + data['endDate'] + ' is not available! Please, consider another one!')
            availabilities.append(availability)
        
        #save booking in database
        savedBookingResponse = super(BookingView,self).create(request,*args,**kwargs)

        #checking if save was ok
        if savedBookingResponse.status_code == 201:
            savedBooking = Booking.objects.get(id=savedBookingResponse.data['id'])
            
            #for each item to be reserved
            for availability in availabilities:
                availability.bookingFK = savedBooking
                availability.save()
            return Response(status=201,data=savedBookingResponse.data)
        else:
            return Response(status=500,data='Error when saving booking!')


class PaymentView(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class =  PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = PaymentFilter
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = None
        if user.is_superuser:
            queryset = Payment.objects.all()
        else:
            #o usuario que solicitou a API tem que ser o mesmo usuario que fez a reserva deste pagamento
            queryset = Payment.objects.filter(bookingFK__customUserFK__user__username=user.username)
        return queryset    


class AvailabilityView(CustomModelViewSet):
    queryset =  Availability.objects.all()
    serializer_class =  AvailabilitySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = AvailabilityFilter
    ordering_fields = '__all__'
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)