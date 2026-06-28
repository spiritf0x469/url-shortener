from django.urls import path
from .views import Shorturlview,Redirectview,Shorturldetailview
urlpatterns=[
    path("shorten/",Shorturlview.as_view(),name="shorten-url"),
    path("<str:short_code>/",Redirectview.as_view(),name="redirect"),
    path("shorten/<int:id>/",Shorturldetailview.as_view()),
]