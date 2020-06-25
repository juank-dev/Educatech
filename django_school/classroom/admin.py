# Django admin
from django.contrib import admin
# local Django
from .models import User, Subject


class ProductAdmin(admin.ModelAdmin):
    """
    Adding the secctions or fields that we want to see in Admin
    """
    fields = ('name', 'description', 'price', 'image')
    list_display = ('__str__', 'slug', 'created_at')



admin.site.register(User)
admin.site.register(Subject, ProductAdmin)