from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Post, Comment

# Create your views here.
def home(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html", context)


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]
    
class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        total_likes = post.total_likes()
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['body']
    template_name = "blog/add_comment.html"  # <app>/<model>_<viewtype>.html
    
    def form_valid(self, form):
        form.instance.name = self.request.user.username
        form.instance.email = self.request.user.email
        post_id = self.kwargs['post_id']
        form.instance.post = get_object_or_404(Post, id=post_id)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['post_id']})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    success_url = "/"   

    
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("post-detail", args=[str(pk)]))

def about(request):
    return render(request, "blog/about.html", {"title": "About"})