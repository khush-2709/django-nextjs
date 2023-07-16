from django.urls import path, include
from .views import GoogleLoginView

urlpatterns = [
  path("google/", GoogleLoginView.as_view(), name = "google"),
]
#from .views import index
#urlpatterns = [
 #  path("", index, name="index"),
#]