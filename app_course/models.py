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
    start_date = models.DateField()
    end_date = models.DateField()

    def save(self, *args, **kwargs):
        if self.teacher.role != UserType.teacher:
            raise ValidationError({"teacher": "User's role must be of type 'teacher'."})
        if self.end_date <= self.start_date:
            raise ValidationError(
                {"end_date": "Course ending date cannot be before the starting date."}
            )

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
                {
                    "time_to": "Event ending time cannot be before the event starting time."
                }
            )

        if self.time_from.date() < self.course.start_date:
            raise ValidationError(
                {
                    "time_from": "Event starting time cannot be before the course's starting date."
                }
            )

        if self.time_to.date() > self.course.end_date:
            raise ValidationError(
                {
                    "time_to": "'Event ending time cannot be after the course's ending date."
                }
            )

        return super().save(*args, **kwargs)
