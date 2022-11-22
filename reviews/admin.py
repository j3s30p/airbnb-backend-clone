from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):

    title = "Filter by Words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("nice", "Nice"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


class RatingFilter(admin.SimpleListFilter):

    title = "Filter by 3+ Reviews!"
    parameter_name = "gte3"

    def lookups(self, request, model_admin):
        return [
            ("high_rate", "High rate"),
            ("low_rate", "Low rate"),
        ]

    def queryset(self, request, reviews):
        rating_filter = self.value()
        if rating_filter == "high_rate":
            return reviews.filter(rating__gte=3)
        elif rating_filter == "low_rate":
            return reviews.filter(rating__lt=3)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
        WordFilter,
        RatingFilter,
    )
