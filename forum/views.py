from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView, CreateView, ListView, DetailView
from .models import Post, Topic
from django.urls import reverse_lazy

# Список тем
class TopicListView(ListView):
    model = Topic

    template_name = "tasks/topic_list.html"
    context_object_name = "topics"

# Деталі конкретної теми
class TopicDetailView(DetailView):
    model = Topic
    template_name = "tasks/topic_details.html"
    context_object_name = "topic"

# Створення нової теми
class TopicCreateView(CreateView):
    model = Topic
    
    template_name = "tasks/topic_create.html"

# Додавання постів до теми
class PostCreateView(CreateView):
    model = Post

    template_name = "tasks/post_create.html"

# Редагування постів до теми
class PostUpdateView(UpdateView):
    model = Post

    success_url = reverse_lazy("topic-list")
    template_name = "tasks/post_update.html"

# Видалення постів до теми
class PostDeleteView(DeleteView):
    model = Post
    template_name = "tasks/post_delete.html"
    success_url = reverse_lazy("topic-list")
    context_object_name = "post"