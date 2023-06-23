from django.db import models
from rest_framework.exceptions import ValidationError
from utilitas.models import BaseModel

from app_auth.models import User, UserType


class Course(BaseModel):
    """
    Represents a course. A course can have many teaching sessions, lab sessions, etc. Those are called Events.
    A teacher can be assigned to many courses. A course cannot have multiple teachers.
    """

    title = models.CharField(max_length=512, unique=True)
    teacher = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="courses"
    )

    def save(self, *args, **kwargs):
        if self.teacher.role != UserType.teacher:
            raise ValidationError({"teacher": "User's role must be of type 'teacher'."})

        return super().save(*args, **kwargs)


class Event(BaseModel):
    """
    An event represents a lecture or a lab session that happens within a Course.
    """

    title = models.CharField(max_length=512)
    time_from = models.DateTimeField()
    time_to = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="events")

    def save(self, *args, **kwargs):
        if self.time_to <= self.time_from:
            raise ValidationError(
                {"time_to": "'time_to' cannot be less than or equal to 'time_from'"}
            )

        return super().save(*args, **kwargs)
