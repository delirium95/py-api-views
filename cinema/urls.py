from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

# Створюємо роутер
router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")

urlpatterns = [
    # Базовий шлях api/cinema/
    path("api/cinema/", include(router.urls)),

    # Додаємо окремо Genre та Actor
    path("api/cinema/genres/", GenreList.as_view(), name="genre-list"),
    path("api/cinema/genres/<int:pk>/",
         GenreDetail.as_view(),
         name="genre-detail"),

    path("api/cinema/actors/", ActorList.as_view(), name="actor-list"),
    path("api/cinema/actors/<int:pk>/",
         ActorDetail.as_view(),
         name="actor-detail"),
]

app_name = "cinema"
