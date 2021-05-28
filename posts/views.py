# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render

# Models
from posts.models import Post


class PostFeedView(LoginRequiredMixin, ListView):

    template_name = 'posts/base.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user=self.request)

        return context