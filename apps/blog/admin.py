from django.contrib import admin
from .models import Blog, Category, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'enabled', 'posted', 'category')  # Display these fields
    list_filter = ('enabled', 'category')  # Filters
    search_fields = ('title',)  # Search functionality


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'blog', 'created_at')
    list_filter = ('blog',)
    search_fields = ('text',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
