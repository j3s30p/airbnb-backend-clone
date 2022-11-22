from rest_framework import serializers
from .models import Perk, Experience
from medias.serializers import PhotoSerializer, VideoSerializer
from wishlists.models import Wishlist
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class TinyPerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = ("name",)


class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperienceListSerializer(serializers.ModelSerializer):

    rating = serializers.SerializerMethodField()
    is_host = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )
    video = VideoSerializer(
        read_only=True,
    )

    class Meta:
        model = Experience
        fields = (
            "pk",
            "name",
            "video",
            "photos",
            "country",
            "city",
            "price",
            "rating",
            "is_host",
            "is_liked",
        )

    def get_rating(self, experience):
        return experience.rating()

    def get_is_host(self, experience):
        request = self.context["request"]
        if request:
            return experience.host == request.user
        return False

    def get_is_liked(self, experience):
        request = self.context["request"]
        if request:
            if request.user.is_authenticated:
                return Wishlist.objects.filter(
                    user=request.user,
                    experiences__id=experience.pk,
                ).exists()
        return False


class ExperienceDetailSerializer(serializers.ModelSerializer):

    host = TinyUserSerializer(
        read_only=True,
    )
    category = CategorySerializer(
        read_only=True,
    )
    rating = serializers.SerializerMethodField()
    is_host = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )
    video = VideoSerializer(
        read_only=True,
    )
    perks = TinyPerkSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Experience
        fields = "__all__"

    def get_rating(self, experience):
        return experience.rating()

    def get_is_host(self, experience):
        request = self.context["request"]
        if request:
            return experience.host == request.user
        return False

    def get_is_liked(self, experience):
        request = self.context["request"]
        if request:
            if request.user.is_authenticated:
                return Wishlist.objects.filter(
                    user=request.user,
                    experiences__id=experience.pk,
                ).exists()
        return False
