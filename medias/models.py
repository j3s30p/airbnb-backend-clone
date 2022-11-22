from django.db import models
from common.models import CommonModel


class Photo(CommonModel):

    """Photo Model Definition"""

    file = models.URLField()
    description = models.CharField(
        max_length=140,
        default="",
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    experiece = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )

    def __str__(self) -> str:
        return "Photo File"


class Video(CommonModel):

    """Video Model Definition"""

    file = models.URLField()
    desciption = models.CharField(
        max_length=140,
        default="",
    )
    experiece = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
        related_name="videos",
    )

    def __str__(self) -> str:
        return "Video File"
