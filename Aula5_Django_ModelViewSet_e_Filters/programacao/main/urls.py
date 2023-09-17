#importando as views que criamos da nossa api:
from .views import *
#importando a DefaultRouter que irá ajudar na definição das rotas da api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people', PeopleAPIView)
router.register(r'planet', PlanetAPIView)
router.register(r'starship', StarshipsAPIView)

urlpatterns = router.urls
