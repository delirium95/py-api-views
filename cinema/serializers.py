from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row")


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    # ManyToMany fields - тільки IDs, без related serializers
    actors = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,  # тільки для створення/оновлення
        required=False,
        default=list
    )

    genres = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,  # тільки для створення/оновлення
        required=False,
        default=list
    )

    def create(self, validated_data):
        # Вилучаємо ManyToMany дані
        actors_ids = validated_data.pop("actors", [])
        genres_ids = validated_data.pop("genres", [])

        # Створюємо фільм
        movie = Movie.objects.create(**validated_data)

        # Додаємо зв'язки ManyToMany
        if actors_ids:
            movie.actors.add(*actors_ids)

        if genres_ids:
            movie.genres.add(*genres_ids)

        return movie

    def update(self, instance, validated_data):
        # Вилучаємо ManyToMany дані
        actors_ids = validated_data.pop("actors", None)
        genres_ids = validated_data.pop("genres", None)

        # Оновлюємо прості поля
        instance.title = validated_data.get("title", instance.title)
        instance.description = (validated_data.
                                get("description", instance.description))
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()

        # Оновлюємо ManyToMany зв'язки, якщо вони передані
        if actors_ids is not None:
            instance.actors.set(actors_ids)

        if genres_ids is not None:
            instance.genres.set(genres_ids)

        return instance
