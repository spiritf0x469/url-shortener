from rest_framework import serializers
from .models import Shorturl
from django.contrib.auth.models import User
class ShorturlSerializer(serializers.ModelSerializer):
    short_url=serializers.SerializerMethodField()
    class Meta:
        model=Shorturl
        fields=["id",
            "owner",
            "original_url",
            "short_code",
            "short_url",
            "clicks",
            "created_at",]
        read_only_fields=["owner","short_code","clicks","created_at",]
    def get_short_url(self,obj):
        request=self.context.get("request")
        if request:
            return request.build_absolute_uri(f"/api/{obj.short_code}/")
        return f"/api/{obj.short_code}/"
class Registerserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password"]
        extra_kwargs={
            "password":{"write_only":True}
        }
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)