from django.contrib import admin

# Register your models here.

from . models import Post

class AreaAdmin(admin.ModelAdmin):
    list_display = ["area", "postcode"]

admin.site.register(Post, AreaAdmin)