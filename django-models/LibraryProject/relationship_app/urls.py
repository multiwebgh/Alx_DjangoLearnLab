from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),   # existing
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),  # existing

    # New authentication routes
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
