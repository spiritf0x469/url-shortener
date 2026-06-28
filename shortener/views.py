from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Shorturl
from .serializers import ShorturlSerializer
from django.shortcuts import get_object_or_404,redirect
import random
import string
# Create your views here.
class Shorturlview(APIView):
    def post(self,request):
        data=request.data.copy()
        code=''.join(random.choices(string.ascii_letters+string.digits,k=6))
        data["short_code"]=code
        serializer=ShorturlSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        urls=Shorturl.objects.all()
        serializer=ShorturlSerializer(urls,many=True)
        return Response(serializer.data)
class Redirectview(APIView):
    def get(self,request,short_code):
        url=get_object_or_404(Shorturl,short_code=short_code)
        url.clicks+=1
        url.save()
        return redirect(url.original_url)
class Shorturldetailview(APIView):
    def delete(self,request,id):
        url=get_object_or_404(Shorturl,id=id)
        url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,id):
        url=get_object_or_404(Shorturl,id=id)
        serializer=ShorturlSerializer(
            url,data=request.data,partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,id):
        url=get_object_or_404(Shorturl,id=id)
        serializer=ShorturlSerializer(url)
        return Response(serializer.data)