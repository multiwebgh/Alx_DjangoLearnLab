from django.urls import path
from blog import views

urlpatterns = [
     path('', views.home, name='home' ),
    #  path('', views.posts, name='home' ),
    #  path('', views.login, name='home' ),
    #  path('', views.register, name='home' ),
]
