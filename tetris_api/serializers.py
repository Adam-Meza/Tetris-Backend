from django.contrib.auth.models import User #uses template MOdel
from rest_framework import serializers
from .models import Game #CUSTOM MODEL

class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} #estavlishes one way write only relationship i.e FRONTEND can make a password but not see it. 
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class GameSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    owner = PublicUserSerializer(source="user", read_only=True)
    user_id = serializers.IntegerField(source="user.id", read_only=True)

    class Meta:
        model = Game
        fields = ["id", "score", "line_count", "created_at", "user", "owner", "user_id"]
        #This protects users/FRONTEND from BACKEND manipulation of data
        read_only_fields = ["created_at", "owner", "user_id"]