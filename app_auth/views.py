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
