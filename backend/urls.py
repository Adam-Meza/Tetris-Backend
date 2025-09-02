from django.contrib import admin
from django.urls import path, include
from tetris_api.views import CreateUserView, AllGamesListCreate, GameListCreate, GameDelete
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("tetris_api/user/register/", CreateUserView.as_view(), name="register"),
    path("tetris_api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("tetris_api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("tetris_api-auth/", include("rest_framework.urls")),

    path("tetris_api/games/", GameListCreate.as_view(), name="games-my"),         
    path("tetris_api/games/all/", AllGamesListCreate.as_view(), name="games-all"),
    path("tetris_api/games/<int:pk>/", GameDelete.as_view(), name="games-delete"),
]
