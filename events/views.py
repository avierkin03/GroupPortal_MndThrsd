from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Event
from .forms import EventForm
from django.urls import reverse_lazy

# Список подій
class EventListView(ListView):
    model = Event
    template_name = "events/events_list.html"
    context_object_name = "events"

# Створення нової події
class EventCreateView(CreateView):
    model = Event
    template_name = "events/event_create.html"
    form_class = EventForm
    success_url = reverse_lazy("event_list")

# Редагування існуючої події
class EventUpdateView(UpdateView):
    model = Event
    template_name = "events/event_update.html"
    form_class = EventForm
    success_url = reverse_lazy("event_list")

# Видалення існуючої події
class EventDeleteView(DeleteView):
    model = Event
    template_name = "events/event_delete.html"
    success_url = reverse_lazy("event_list")