"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tetris_api.views import CreateUserView, AllGamesListCreate, GameListCreate, GameDelete
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),

    # auth & users
    path("tetris_api/user/register/", CreateUserView.as_view(), name="register"),
    path("tetris_api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("tetris_api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("tetris_api-auth/", include("rest_framework.urls")),

    # games
    path("tetris_api/games/", GameListCreate.as_view(), name="games-my"),         # GET (mine, auth) + POST (auth)
    path("tetris_api/games/all/", AllGamesListCreate.as_view(), name="games-all"),# GET (public)
    path("tetris_api/games/<int:pk>/", GameDelete.as_view(), name="games-delete"),
]
