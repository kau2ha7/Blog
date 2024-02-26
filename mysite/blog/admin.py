from django.contrib import admin
from .models import Post,Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author','title','published_date']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','author']
    
    
