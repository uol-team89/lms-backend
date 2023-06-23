from django.urls import path

from app_course import views

urlpatterns = [
    path("courses", views.CourseListView.as_view(), name="course-list"),
    path(
        "courses/<int:obj_id>", views.CourseDetailsView.as_view(), name="course-details"
    ),
    path("courses/search", views.CourseSearchView.as_view(), name="course-search"),
    path("events", views.EventListView.as_view(), name="event-list"),
    path("events/<int:obj_id>", views.EventDetailsView.as_view(), name="event-details"),
    path("events/search", views.EventSearchView.as_view(), name="event-search"),
]
