from django.urls import path
from .views import Shorturlview,Redirectview,Shorturldetailview,Registerview
urlpatterns=[
    path("shorten/",Shorturlview.as_view(),name="shorten-url"),
    path("shorten/<int:id>/",Shorturldetailview.as_view()),
    path("register/",Registerview.as_view(),name="register",),
    path("<str:short_code>/",Redirectview.as_view(),name="redirect"),
]