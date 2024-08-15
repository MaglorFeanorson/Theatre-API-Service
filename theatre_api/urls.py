from django.urls import path, include
from rest_framework import routers

from theatre_api.views import (
    ActorViewSet,
    GenreViewSet,
    PlayViewSet,
    PerformanceViewSet,
    ReservationViewSet,
    TheatreHallViewSet,
    TicketViewSet,
)


router = routers.DefaultRouter()
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("plays", PlayViewSet)
router.register("performances", PerformanceViewSet)
router.register("reservations", ReservationViewSet)
router.register("theatre_hall", TheatreHallViewSet)
router.register("tickets", TicketViewSet)

urlpatterns = router.urls

app_name = "theatre_api"
