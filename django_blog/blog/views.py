from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm, UserUpdateForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm

# List all posts (public)
class PostListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'   # templates/blog/posts_list.html
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 10  # optional

# Detail view for a single post (public)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # templates/blog/post_detail.html
    context_object_name = 'post'

# Create view - only logged-in users
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'  # templates/blog/post_form.html

    def form_valid(self, form):
        # set the logged-in user as the author
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update view - only author can edit
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

# Delete view - only author can delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('posts')  # redirect to posts list

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


# Create your views here.

def home(request):
    
    return render(request, "index.html")


def posts(request):
    return render(request, 'posts.html')


# Register View
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

# Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})

# Login View (using Django’s built-in)
class UserLoginView(LoginView):
    template_name = 'blog/login.html'

# Logout View (using Django’s built-in)
class UserLogoutView(LogoutView):
    template_name = 'blog/logout.html'
