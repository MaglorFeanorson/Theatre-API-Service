from rest_framework import serializers

from theatre_api.models import (
    Actor,
    Genre,
    Play,
    Performance,
    Reservation,
    TheatreHall,
    Ticket,
)


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("id", "created_at", "user")


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_rows",
            "num_seats",
        )


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name", "image")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ("id", "title", "description", "genre", "actors", "image")


class PlayListSerializer(PlaySerializer):
    genre = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Play
        fields = (
            "id",
            "title",
            "description",
            "genre",
            "actors",
            "image",
        )


class PlayDetailSerializer(PlaySerializer):
    genre = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Play
        fields = (
            "id",
            "title",
            "description",
            "genre",
            "actors",
            "image",
        )


class PlayImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ("id", "image")


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ("id", "play", "theatre_hall", "show_time")


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "performance")
