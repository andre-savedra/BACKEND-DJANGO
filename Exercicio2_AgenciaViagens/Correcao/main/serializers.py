from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        many = True

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        many = True

class ImageSerializer(serializers.ModelSerializer):
    tripFK = TripSerializer(read_only=True)
    class Meta:
        model = Image
        fields = '__all__'
        many = True

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','is_superuser','first_name','last_login')
        many = True

class CustomUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = CustomUser
        fields = '__all__'
        many = True

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        many = True

class PaymentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Payment
        fields = '__all__'
        many = True

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'
        many = True