from atexit import register
from re import search
from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','new_category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published', 'is_published')
    list_filter = ('new_category','is_published' )
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    
 
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

