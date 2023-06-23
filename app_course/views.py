from utilitas.views import BaseDetailsView, BaseListView, BaseSearchView

from app_course import models, serializers


class CourseListView(BaseListView):
    name = "Course list view"
    model = models.Course
    serializer = serializers.CourseSerializer


class CourseDetailsView(BaseDetailsView):
    name = "Course details view"
    model = models.Course
    serializer = serializers.CourseSerializer


class CourseSearchView(BaseSearchView):
    name = "Course search view"
    model = models.Course
    serializer = serializers.CourseSerializer


class EventListView(BaseListView):
    name = "Event list view"
    model = models.Event
    serializer = serializers.EventSerializer


class EventDetailsView(BaseDetailsView):
    name = "Event details view"
    model = models.Event
    serializer = serializers.EventSerializer


class EventSearchView(BaseSearchView):
    name = "Event search view"
    model = models.Event
    serializer = serializers.EventSerializer
