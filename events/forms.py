from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta():
        model = Event
        fields = ["title", "start_time", "end_time", "description"]
        widgets = {
            "title": forms.TextInput(),
            "start_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "end_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "description": forms.Textarea()
        }