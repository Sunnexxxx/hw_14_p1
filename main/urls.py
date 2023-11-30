from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import all_posts, post_detail, create_post, delete_post, post_update

urlpatterns = [
    path('', all_posts, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('create_post/', create_post, name='create_post'),
    path('delete_post/<int:pk>/', delete_post, name='post_delete'),
    path('post/<int:pk>/update/', post_update, name='post_update')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)