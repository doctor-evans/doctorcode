from . import views
from django.urls import path

urlpatterns = [
    path("", views.indexView, name="home"),
    path("blog/", views.allPost, name="blog"),
    path("video-downloader/", views.downloadView, name="downloader"),
    path("about-us/", views.aboutUsView, name="aboutus"),
    path("blog/<slug:slug>/", views.post_detail, name="post_detail"),
]