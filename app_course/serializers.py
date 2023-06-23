from utilitas.serializers import BaseModelSerializer

from app_course import models


class CourseSerializer(BaseModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"
        expandable_fields = {
            "teacher": "app_auth.serializers.UserSerializer",
            "events": ("app_course.serializers.EventSerializer", {"many": True}),
        }


class EventSerializer(BaseModelSerializer):
    class Meta:
        model = models.Event
        fields = "__all__"
        expandable_fields = {"course": "app_course.serializers.CourseSerializer"}
