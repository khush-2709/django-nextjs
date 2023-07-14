from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path("<str:username>/", views.getUserInfo),
    path("getmediainsights/<media_id>/", views.getMediaInsights)
]
