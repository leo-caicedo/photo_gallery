# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy

# Models
from posts.models import Post


class PostFeedView(LoginRequiredMixin, ListView):

    template_name = 'posts/base.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user=self.request.user)

        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    
    model = Post
    fields = ['title', 'photo']
    success_url = reverse_lazy('posts:feed')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):

    model = Post
    fields = ['title', 'photo']
    success_url = reverse_lazy('posts:feed')


class PostDeleteView(LoginRequiredMixin, DeleteView):

    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('posts:feed')