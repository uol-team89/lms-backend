path("events", views.EventListView.as_view(), name="event-list"),
path("events/<int:obj_id>", views.EventDetailsView.as_view(), name="event-details"),
path("events/search", views.EventSearchView.as_view(), name="event-search"),
