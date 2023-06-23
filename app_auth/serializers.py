from utilitas.serializers import BaseModelSerializer

from app_auth.models import User


class UserSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}
        expandable_fields = {
            "courses": ("app_course.serializers.CourseSerializer", {"many": True})
        }

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.save()

        return user
