from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book


class BookAPITest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client.login(username="testuser", password="testpass123")

        # Create a sample book
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            publication_year=2023
        )

        # Endpoints
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Book", response.content.decode())

    def test_create_book(self):
        data = {"title": "New Book", "author": "New Author", "publication_year": 2024}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        data = {"title": "Updated Book", "author": "Updated Author", "publication_year": 2025}
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        response = self.client.get(f"{self.list_url}?author=Test Author")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Author", response.content.decode())

    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Book", response.content.decode())

    def test_order_books(self):
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Test Book")