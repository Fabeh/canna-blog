from django.shortcuts import render
from django.utils import timezone
# Dot = current dir. Imports the Post model.
from .models import Post

""" More Info on QuerySets:
 https://tutorial.djangogirls.org/en/django_orm/
 https://docs.djangoproject.com/en/1.9/ref/models/querysets/ """

# Put together Blog/post_list.html template
def post_list(request):
     # QuerySet
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
