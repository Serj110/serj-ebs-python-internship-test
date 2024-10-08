from rest_framework import serializers

from apps.blog.models import Blog, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'body', 'posted', 'category', 'enabled', 'comments']


    def validate_enabled(self, value):
        if not isinstance(value, bool):
            raise serializers.ValidationError("Enabled must be a boolean value.")
        return value


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'blog', 'created_at']

    def create(self, validated_data):
        blog_id = validated_data.pop('blog_id')
        blog = Blog.objects.get(id=blog_id)
        comment = Comment.objects.create(blog=blog, **validated_data)
        return comment


class BlogDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'body', 'posted', 'category', 'enabled', 'comments']
