from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('djoser.urls')), #adiciona as rotas de gerenciamento de usuarios
    path('auth/', include('djoser.urls.authtoken')), #adiciona a rota de obter token
]
