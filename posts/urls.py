# Django
from django.urls import path

# Views
from posts.views import PostFeedView, PostCreateView, PostUpdateView

app_name = 'posts'
urlpatterns = [
    path('', PostFeedView.as_view(), name='feed'),
    path('create', PostCreateView.as_view(), name='create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update')
]