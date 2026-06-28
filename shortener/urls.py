from django.urls import path
from .views import Shorturlview
urlpatterns=[path("shorten/",Shorturlview.as_view(),name="shorten-url"),]