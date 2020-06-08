from django.contrib import admin
from .models import Thread, ChatMessage

class ChatMessagea(admin.TabularInline):
    model = ChatMessage

class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessagea]
    list_display = ("first", "second", "updated")
    #search_fields = ("first", "second")
    list_filter = ("first", "second","updated")
    date_hierarchy="updated"

    class Meta:
        model = Thread 
class ChatAdmin(admin.ModelAdmin):
    list_display = ("thread", "user", "message", "timestamp")
    list_filter = ("user", "timestamp")



admin.site.register(Thread, ThreadAdmin)
admin.site.register(ChatMessage, ChatAdmin)