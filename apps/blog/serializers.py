from rest_framework import serializers

from apps.blog.models import Blog, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

    def validate_enabled(self, value):
        if not isinstance(value, bool):
            raise serializers.ValidationError("Enabled must be a boolean value.")
        return value

