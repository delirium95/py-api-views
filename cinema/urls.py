from django.urls import path, include
from rest_framework import routers

from cinema.views import (MovieViewSet,
                          CinemaHallViewSet,
                          GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail)

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    # Genre endpoints - APIView
    path("api/cinema/genres/", GenreList.as_view(), name="genre-list"),
    path("api/cinema/genres/<int:pk>/",
         GenreDetail.as_view(), name="genre-detail"),

    # Actor endpoints - GenericAPIView
    path("api/cinema/actors/", ActorList.as_view(), name="actor-list"),
    path("api/cinema/actors/<int:pk>/",
         ActorDetail.as_view(), name="actor-detail"),

    # Include router URLs for CinemaHall and Movie
    path("api/cinema/", include(router.urls)),
]

app_name = "cinema"
