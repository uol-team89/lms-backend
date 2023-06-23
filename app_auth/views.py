from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from utilitas.views import BaseDetailsView, BaseListView, BaseSearchView

from app_auth import models, serializers


class UserListView(BaseListView):
    model = models.User
    serializer = serializers.UserSerializer


class UserDetailsView(BaseDetailsView):
    model = models.User
    serializer = serializers.UserSerializer


class UserSearchView(BaseSearchView):
    model = models.User
    serializer = serializers.UserSerializer


class LoginView(TokenObtainPairView):
    name = "The login endpoint"
    serializer_class = TokenObtainPairSerializer
