from django.urls import path
from . import views

urlpatterns = [
    path("", views.EventListView.as_view(), name="event_list"),
    path("", views.EventCreateView.as_view(), name="event_create"),
    path("", views.EventUpdateView.as_view(), name="event_update"),
    path("", views.EventDeleteView.as_view(), name="event_delete"),
]