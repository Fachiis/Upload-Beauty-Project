from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'postlist'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "post.html"
    success_url = reverse_lazy('home')
    




