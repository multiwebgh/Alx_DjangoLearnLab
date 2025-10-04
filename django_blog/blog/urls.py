from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('posts/', views.posts, name='posts'),
    path('register/', views.register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]
