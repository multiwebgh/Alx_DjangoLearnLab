from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),  # list view (homepage for posts)
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),  # create new post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # single post view
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),  # update post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # delete post
]
