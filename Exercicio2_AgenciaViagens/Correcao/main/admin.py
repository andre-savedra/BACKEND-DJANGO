from django.contrib import admin
from .models import *

class adminCategory(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Category, adminCategory)


class adminTrip(admin.ModelAdmin):
    list_display = ('id', 'title', 'city', 'createdDate')
    list_display_links = ('id', 'title', 'city', 'createdDate',)
    search_fields = ('title', 'city', 'address')
    list_per_page = 10

admin.site.register(Trip, adminTrip)


class adminImage(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    list_per_page = 10

admin.site.register(Image, adminImage)


class adminCustomUser(admin.ModelAdmin):
    list_display = ('id', 'address', 'taxId')
    list_display_links = ('id', 'address', 'taxId',)
    search_fields = ('address', 'taxId',)
    list_per_page = 10

admin.site.register(CustomUser, adminCustomUser)


class adminBooking(admin.ModelAdmin):
    list_display = ('id', 'tripFK', 'startDate', 'endDate' , 'purchaseValue')
    list_display_links = ('id', 'tripFK', 'startDate', 'endDate' , 'purchaseValue',)
    search_fields = ('purchaseValue', 'tripFK', 'comment',)
    list_per_page = 10

admin.site.register(Booking, adminBooking)


class adminPayment(admin.ModelAdmin):
    list_display = ('id', 'data', 'value', 'status' )
    list_display_links = ('id', 'data', 'value', 'status',)
    search_fields = ('data', 'value', 'status',)
    list_per_page = 10

admin.site.register(Payment, adminPayment)


class adminAvailability(admin.ModelAdmin):
    list_display = ('id', 'tripFK', 'bookingFK', 'date' )
    list_display_links = ('id', 'tripFK', 'bookingFK', 'date',)
    search_fields = ('date',)
    list_per_page = 10

admin.site.register(Availability, adminAvailability)

