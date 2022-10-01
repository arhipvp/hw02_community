from calendar import c
from django.contrib import admin
from pkg_resources import empty_provider
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pub_date', 'author_id')
    list_filter = ('pub_date', 'author_id')
    empty_value_display = 'Тут пока ничего нет'
    
admin.site.register(Post, PostAdmin)