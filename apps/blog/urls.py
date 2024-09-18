from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.blog.views import BlogItemView, BlogListView, CategoryViewSet, BlogCreateView, CommentCreateView, BlogDetailView

router = DefaultRouter(trailing_slash=False)
router.register(
    r"blog/categories",
    CategoryViewSet,
    basename="category",
)

urlpatterns = [
    path("blog", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>", BlogItemView.as_view(), name="blog-detail"),
    *router.urls,
    path('_new_api/blogs/', BlogCreateView.as_view(), name='blog-create'),
    path('_new_api/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('_new_api/blog&comments/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]
