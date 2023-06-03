from django.contrib import admin
from .models import UserManager, User, Story, Comment

# Register your models here.


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'section', 'created_at') 
  
    search_fields = ('section', 'author', 'keyword', 'content') 
       
    prepopulated_fields = {'slug':('title', 'content')}
    
    # Arrangement or customising django admin dashboard
    # fields = ('title', 'content', 'slug')
    
    # if you want to display 'title' and 'slug' on the same row; 
    # fields = (('title', 'slug'), 'content')
    
admin.site.register(Story, StoryAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'story', 'content', 'created_at') 
    search_fields = ('user', 'story', 'content')
    
admin.site.register(Comment, CommentAdmin)


