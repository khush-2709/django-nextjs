from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path("<str:username>/", views.getUserInfo),
    path("getphotovideoinsights/<int:media_id>/", views.getPhotoVideoInsights),
    path("getreelsinsights/<int:media_id>/", views.getReelsInsights),
    path("getstoryinsights/<int:media_id>/", views.getStoryInsights),
    path("getuserinsights/<int:userid>/", views.getUserInsights),
    path("getmediacomments/<int:media_id>/", views.getMediaComments),
]
