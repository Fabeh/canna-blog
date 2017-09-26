from django.contrib import admin

# Methods from models.py
from .models import Post

# Register Models here
admin.site.register(Post)
