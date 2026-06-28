from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Shorturl
from .serializers import ShorturlSerializer
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