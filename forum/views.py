from django.shortcuts import render

# Список тем
class TopicListView():

    template_name = "tasks/topic_list.html"

# Деталі конкретної теми
class TopicDetailView():

    template_name = "tasks/topic_details.html"

# Створення нової теми
class TopicCreateView():
    
    template_name = "tasks/topic_create.html"

# Додавання постів до теми
class PostCreateView():

    template_name = "tasks/post_create.html"

# Редагування постів до теми
class PostUpdateView():

    template_name = "tasks/post_update.html"

# Видалення постів до теми
class PostDeleteView():

    template_name = "tasks/post_delete.html"