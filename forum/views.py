from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView, CreateView, ListView, DetailView
from .forms import PostForm, TopicForm
from .models import Post, Topic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Список тем
class TopicListView(ListView):
    model = Topic

    template_name = "forum/topic_list.html"
    context_object_name = "topics"

# Деталі конкретної теми
class TopicDetailView(DetailView):
    model = Topic
    template_name = "forum/topic_details.html"
    context_object_name = "topic"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PostForm()
        context["posts"] = self.object.posts.all()
        return context

# Створення нової теми
class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy("topic-list")
    template_name = "forum/topic_create.html"
    def form_valid(self, Form):
        Form.instance.creator = self.request.user
        return super().form_valid(Form)

# Додавання постів до теми
class PostCreateView(CreateView):
    model = Post
    success_url = reverse_lazy("topic-list")
    form_class = PostForm
    def form_valid(self, Form):
        Form.instance.creator = self.request.user
        Form.instance.topic = Topic.objects.get(pk = self.kwargs["pk"])
        return super().form_valid(Form)
#    template_name = "tasks/post_create.html"

# Редагування постів до теми
class PostUpdateView(UpdateView):
    model = Post

    success_url = reverse_lazy("topic-list")
    template_name = "forum/post_update.html"

# Видалення постів до теми
class PostDeleteView(DeleteView):
    model = Post
    template_name = "forum/post_delete.html"
    success_url = reverse_lazy("topic-list")
    context_object_name = "post"