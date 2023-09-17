from django.contrib import admin
from .models import * #importando o People e o Planet!!!

# Register your models here.

class detPeople(admin.ModelAdmin):
    list_display = ('id', 'name', 'hairColor')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 10

#registra as configurações realizadas do model na página de admin
admin.site.register(People,detPeople)



class detPlanet(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 10

#registra as configurações realizadas do model na página de admin
admin.site.register(Planet,detPlanet)


class detStarship(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10

#registra as configurações realizadas do model na página de admin
admin.site.register(Starships,detStarship)