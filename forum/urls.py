from django.urls import path
from . import views

urlpatterns = [
    path("", views.TopicListView.as_view(), name="topic-list"),
    path("topic-detail/<int:pk>/", views.TopicDetailView.as_view(), name="topic-detail"),
    path("topic-create/", views.TopicCreateView.as_view(), name="topic-create"),
    path("post-create/<int:pk>/", views.PostCreateView.as_view(), name="post-create"),
    path("post-update/<int:pk>/", views.PostUpdateView.as_view(), name="post-update"),
    path("post-delete/<int:pk>/", views.PostDeleteView.as_view(), name="post-delete"),
]