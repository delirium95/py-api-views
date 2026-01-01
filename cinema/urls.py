from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    movie_list,
    movie_detail,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

# Створюємо роутер для ViewSet
router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")
# УВАГА: Не реєструємо movies тут, бо вони вже є через функції

urlpatterns = [
    # Всі URL мають префікс api/cinema/

    # Movies - через функції
    path("api/cinema/movies/", movie_list, name="movie-list"),
    path("api/cinema/movies/<int:pk>/", movie_detail, name="movie-detail"),

    # Genre - APIView
    path("api/cinema/genres/", GenreList.as_view(), name="genre-list"),
    path("api/cinema/genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),

    # Actor - GenericAPIView
    path("api/cinema/actors/", ActorList.as_view(), name="actor-list"),
    path("api/cinema/actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

    # CinemaHall - GenericViewSet через роутер
    path("api/cinema/", include(router.urls)),
]

app_name = "cinema"
