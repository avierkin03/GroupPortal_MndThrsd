from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Event

# Список подій
class EventListView(ListView):
    model = Event
    template_name = "events/events_list.html"
    context_object_name = "events"

# Створення нової події
class EventCreateView(CreateView):
    model = Event
    template_name = "events/event_create.html"

# Редагування існуючої події
class EventUpdateView(UpdateView):
    model = Event
    template_name = "events/event_update.html"

# Видалення існуючої події
class EventDeleteView(DeleteView):
    model = Event
    template_name = "events/event_delete.html"