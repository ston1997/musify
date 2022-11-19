from rest_framework import serializers
from music.models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "id",
            "title"
        )


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = (
            "id",
            "name"
        )


class TrackDetailSerializer(serializers.ModelSerializer):
    singer = SingerSerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = Track
        fields = (
            'title',
            'singer',
            'genre',
            'rating',

        )


class TrackListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    number_of_singers = serializers.SerializerMethodField()

    class Meta:
        model = Track
        fields = (
            "title",
            "rating",
            "genres",
            "number_of_singers"
        )

    @staticmethod
    def get_number_of_tracks(obj):
        return obj.track.all().count()


class AlbumDetailSerializer(serializers.ModelSerializer):
    singers = SingerSerializer(many=True)
    tracks = TrackListSerializer(many=True)

    class Meta:
        model = Album
        fields = (
            'title'
            'singers'
            'tracks'
        )
