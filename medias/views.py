from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Photo, Video


class PhotoDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise NotFound

    def delete(self, request, pk):
        photo = self.get_object(pk)
        if (photo.room and photo.room.owner != request.user) or (
            photo.experiece and photo.experiece.host != request.user
        ):
            raise PermissionDenied
        photo.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class VideoDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise NotFound

    def delete(self, request, pk):
        video = self.get_object(pk)
        if video.experiece and video.experiece.host != request.user:
            raise PermissionDenied
        video.delete()
        return Response(status=HTTP_204_NO_CONTENT)
