from rest_framework import serializers
from .models import Room, Amenity
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist


class TinyAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ("name",)


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomListSerializer(serializers.ModelSerializer):

    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
            "is_liked",
            "photos",
        )

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        if request:
            return room.owner == request.user
        return False

    def get_is_liked(self, room):
        request = self.context["request"]
        if request:
            if request.user.is_authenticated:
                return Wishlist.objects.filter(
                    user=request.user,
                    rooms__id=room.pk,
                ).exists()
        return False


class RoomDetailSerializer(serializers.ModelSerializer):

    owner = TinyUserSerializer(
        read_only=True,
    )
    category = CategorySerializer(
        read_only=True,
    )

    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )
    amenities = TinyAmenitySerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Room
        fields = "__all__"

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        if request:
            return room.owner == request.user
        return False

    def get_is_liked(self, room):
        request = self.context["request"]
        if request:
            if request.user.is_authenticated:
                return Wishlist.objects.filter(
                    user=request.user,
                    rooms__id=room.pk,
                ).exists()
        return False
