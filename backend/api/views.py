# insta api required modules
import os
import json
from .instaAPI.api import MetaGraphAPI
from dotenv import load_dotenv, dotenv_values

# django specific modules
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


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
    return Response(response["json_data"])


@api_view()
def getMediaInsights(request, media_id):
    # print(api.getLatestUserMediaID('programminganytime'))
    response = api.getMediaInsights((media_id), debug="yes")
    insightsAnalytics = dict()
    for insight in response["json_data"]["data"]:
        insightsAnalytics[insight["name"]] = insight["values"][0]["value"]
    return Response(insightsAnalytics)
