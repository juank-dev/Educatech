from django.contrib import admin
from .models import User, Subject


class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'price', 'image')
    list_display = ('__str__', 'slug', 'created_at')



admin.site.register(User)
admin.site.register(Subject, ProductAdmin)