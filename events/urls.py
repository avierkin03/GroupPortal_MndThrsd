from django.urls import path
from . import views

urlpatterns = [
    path("", views.EventListView.as_view(), name="event_list"),
    path("event_create/", views.EventCreateView.as_view(), name="event_create"),
    path("event_update/<int:pk>", views.EventUpdateView.as_view(), name="event_update"),
    path("event_delete/<int:pk>", views.EventDeleteView.as_view(), name="event_delete"),
]