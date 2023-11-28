from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import all_posts, post_detail, create_post

urlpatterns = [
    path('', all_posts, name='all_posts'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('create_post/', create_post, name='create_post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)