from django.contrib import admin
from .models import Post, Group


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
