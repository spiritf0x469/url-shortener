from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Shorturl
from .serializers import ShorturlSerializer
from django.shortcuts import get_object_or_404,redirect
from .utils import generate_short_code
from .serializers import Registerserializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class Shorturlview(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data.copy()
        code=generate_short_code()
        serializer=ShorturlSerializer(data=data,context={"request":request})
        if serializer.is_valid():
            serializer.save(owner=request.user,short_code=code,)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        urls=Shorturl.objects.filter(owner=request.user)
        serializer=ShorturlSerializer(urls,many=True,context={"request":request})
        return Response(serializer.data)
class Redirectview(APIView):
    def get(self,request,short_code):
        url=get_object_or_404(Shorturl,short_code=short_code)
        url.clicks+=1
        url.save()
        return redirect(url.original_url)
class Shorturldetailview(APIView):
    permission_classes=[IsAuthenticated]
    def delete(self,request,id):
        url=get_object_or_404(Shorturl,id=id,owner=request.user)
        url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,id):
        url=get_object_or_404(Shorturl,id=id,owner=request.user)
        serializer=ShorturlSerializer(
            url,data=request.data,partial=True,context={"request":request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,id):
        url=get_object_or_404(Shorturl,id=id,owner=request.user)
        serializer=ShorturlSerializer(url,context={"request":request})
        return Response(serializer.data)
class Registerview(APIView):
    def post(self,request):
        serializer=Registerserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)