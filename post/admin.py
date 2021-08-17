from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from .models import Post, Chatroom

# Register your models here.

class PostAdmin(GroupAdmin):
    list_display = ('author', 'roomname', 'text', 'send_at')
    readonly_fields = ('id', 'roomname', 'room', 'authorname', 'text', 'author', 'send_at')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ()

class ChatroomAdmin(GroupAdmin):
    list_display = ('room_name', 'created_by', 'created_at')
    readonly_fields = ('id', 'created_by', 'room_name', 'creator', 'created_at')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ()

admin.site.register(Post,PostAdmin)
admin.site.register(Chatroom, ChatroomAdmin)