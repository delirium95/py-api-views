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

# Створюємо роутер для Movie (ModelViewSet)
movie_router = routers.DefaultRouter()
movie_router.register("movies", MovieViewSet, basename="movie")

# Для CinemaHall теж використовуємо роутер
cinema_hall_router = routers.DefaultRouter()
cinema_hall_router.register("cinema_halls",
                            CinemaHallViewSet,
                            basename="cinema-hall")

urlpatterns = [
    # Базовий шлях api/cinema/

    # Включаємо роутери для Movie та CinemaHall
    path("api/cinema/", include(movie_router.urls)),
    path("api/cinema/", include(cinema_hall_router.urls)),

    # Genre та Actor - окремі класи
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
