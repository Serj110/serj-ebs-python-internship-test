from django.contrib import admin
from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'enabled', 'posted', 'category')  # Display these fields
    list_filter = ('enabled', 'category')  # Filters
    search_fields = ('title',)  # Search functionality


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')  # Display fields for categories
    prepopulated_fields = {'slug': ('title',)}  # Auto-populate slug from title


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

