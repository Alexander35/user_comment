from django.contrib import admin

# Register your models here.
from .models import Town, Region, Comment

admin.site.register(Town)
admin.site.register(Region)
admin.site.register(Comment)
