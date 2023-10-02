
from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'category',CategoryView)
router.register(r'trip',TripView)
router.register(r'image',ImageView)
router.register(r'customUser',CustomUserView)
router.register(r'booking',BookingView)
router.register(r'payment',PaymentView)
router.register(r'availability',AvailabilityView)

urlpatterns = router.urls
urlpatterns.append( path('tripScore/<int:tripId>/', ScoreAverageView.as_view(), name='trip-score-average'))

