from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('posts/', views.posts, name='posts'),
    path('register/', views.register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    # create new post
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    # detail
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    # edit
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    # delete
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
