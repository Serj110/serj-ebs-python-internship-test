from django.contrib import admin

from apps.blog.models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_enabled')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Blog)
admin.site.register(Category)
