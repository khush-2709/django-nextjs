# insta api required modules
import os
import json
from .instaAPI.api import MetaGraphAPI
from dotenv import load_dotenv, dotenv_values
import requests

# django specific modules
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def extractInsights(response):
    userInsightsAnalytics = dict()
    for insight in response["json_data"]["data"]:
        userInsightsAnalytics[insight["name"]] = insight["total_value"]["value"]
    return userInsightsAnalytics


load_dotenv()


api = MetaGraphAPI(
    LONG_LIVED_TOKEN=os.getenv("LONG_LIVED_ACCESS_TOKEN"),
    CLIENT_ID=os.getenv("CLIENT_ID"),
    CLIENT_SECRET=os.getenv("CLIENT_SECRET"),
    BASE_URL=os.getenv("BASE_URL"),
    API_VERSION=os.getenv("API_VERSION"),
    FB_PAGE_ID=os.getenv("FB_PAGE_ID"),
    DEV_INSTA_ID=os.getenv("DEV_INSTA_ID"),
    DEV_INSTA_USERNAME=os.getenv("DEV_INSTA_USERNAME"),
)


# Create your views here.
@api_view()
def getUserInfo(request, username):
    response = api.getUserInfo(username, debug="no")
    return Response(response["json_data"]["business_discovery"])


@api_view()
def getPhotoVideoInsights(request, media_id):
    response = api.getPhotoVideoInsights((media_id), debug="no")
    photovideoAnalytics = dict()
    for insight in response["json_data"]["data"]:
        photovideoAnalytics[insight["name"]] = insight["values"][0]["value"]
    return Response(photovideoAnalytics)


@api_view()
def getReelsInsights(request, media_id):
    response = api.getReelsInsights((media_id), debug="no")
    reelsAnalytics = dict()
    for insight in response["json_data"]["data"]:
        reelsAnalytics[insight["name"]] = insight["values"][0]["value"]
    return Response(reelsAnalytics)


@api_view()
def getStoryInsights(request, media_id):
    response = api.getStoryInsights((media_id), debug="no")
    storyAnalytics = dict()
    for insight in response["json_data"]["data"]:
        storyAnalytics[insight["name"]] = insight["values"][0]["value"]
    return Response(storyAnalytics)


@api_view()
def getUserInsights(request, userid):
    response = api.getUserInsights((userid), debug="no")
    # refining the response
    userInsightsAnalytics = dict()
    count = 0
    insights = list()
    while count < 10:
        insights.insert(0,extractInsights(response))
        print(insights)
        print(response["json_data"]["paging"])
        response = api.makeApiCall(response["json_data"]["paging"]["previous"])
        count = count + 1
    return Response(insights)


@api_view()
def getMediaComments(request, media_id):
    response = api.getMediaComments(media_id, debug="no")
    return Response(response["json_data"]["data"])
