from calendar import c
from django.contrib import admin
from pkg_resources import empty_provider
from .models import Post, Group

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
        'pub_date',
        'author_id',
        'group',
    )
    search_fields = ('text',)
    list_filter = ('pub_date', 'author_id')
    empty_value_display = '-пусто-'
    list_editable = ('group',)
    
admin.site.register(Post, PostAdmin)
admin.site.register(Group)