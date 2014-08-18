from django.contrib import admin

from .models import Post, Tag, Category

# admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)

from django_markdown.admin import MarkdownModelAdmin
admin.site.register(Post, MarkdownModelAdmin)