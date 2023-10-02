from rest_framework import filters
import django_filters

from .models import *


class CategoryFilter(django_filters.FilterSet):
   name = django_filters.CharFilter(lookup_expr='icontains')

   class Meta:
      model = Category
      fields = ['name']


class TripFilter(django_filters.FilterSet):
   title = django_filters.CharFilter(lookup_expr='icontains')
   city = django_filters.CharFilter(lookup_expr='icontains')
   address = django_filters.CharFilter(lookup_expr='icontains')
   daily = django_filters.RangeFilter()

   class Meta:
      model = Trip
      fields = ['title','city','address','daily']


class CustomUserFilter(django_filters.FilterSet):
   taxId = django_filters.CharFilter(lookup_expr='icontains')
   address = django_filters.CharFilter(lookup_expr='icontains')

   class Meta:
      model = CustomUser
      fields = ['taxId','address']


class BookingFilter(django_filters.FilterSet):
   startDate = django_filters.DateFilter(lookup_expr='gte')
   endDate = django_filters.DateFilter(lookup_expr='lte')
   purchaseValue = django_filters.RangeFilter()
   status = django_filters.CharFilter(lookup_expr='exact')

   class Meta:
      model = Booking
      fields = ['startDate','endDate','purchaseValue','status']


class PaymentFilter(django_filters.FilterSet):
   value = django_filters.RangeFilter()
   category = django_filters.CharFilter(lookup_expr='icontains')
   status = django_filters.CharFilter(lookup_expr='icontains')

   class Meta:
      model = Payment
      fields = ['value','category','status']


class AvailabilityFilter(django_filters.FilterSet):
   date = django_filters.RangeFilter()

   class Meta:
      model = Availability
      fields = ['date']
