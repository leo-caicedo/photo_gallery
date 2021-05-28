# Django
from django.urls import path

# Views
from posts.views import PostFeedView

app_name = 'posts'
urlpatterns = [
    path('', PostFeedView.as_view(), name='feed')
]