from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny  
from .models import Game
from .serializers import UserSerializer, GameSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response

class GameListCreate(generics.ListCreateAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Game.objects.filter(user=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AllGamesListCreate(generics.ListAPIView):
    serializer_class = GameSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_queryset(self):
        return Game.objects.all().order_by("-created_at")

class GameDelete(generics.DestroyAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Game.objects.filter(user=self.request.user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
