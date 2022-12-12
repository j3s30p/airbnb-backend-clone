from django.urls import path
from . import views

urlpatterns = [
    path("photos/get-url", views.GetUploadURL.as_view()),
    path("photos/<int:pk>", views.PhotoDetail.as_view()),
    path("videos/<int:pk>", views.VideoDetail.as_view()),
]
