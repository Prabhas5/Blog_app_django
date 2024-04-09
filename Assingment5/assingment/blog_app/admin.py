from django.contrib import admin

from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'published_date')
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','post', 'author', 'created_date')
    list_filter = ('post', 'author', 'created_date')
    search_fields = ('text',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
