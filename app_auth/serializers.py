from utilitas.serializers import BaseModelSerializer

from app_auth.models import User


class UserSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.save()

        return user
