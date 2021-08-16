from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from .models import Post

# Register your models here.

class PostAdmin(GroupAdmin):
    list_display = ('authorname', 'text', 'author', 'send_at')
    readonly_fields = ('id', 'authorname', 'text', 'author', 'send_at')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ()

#admin.site.unregister(Post)
admin.site.register(Post,PostAdmin)