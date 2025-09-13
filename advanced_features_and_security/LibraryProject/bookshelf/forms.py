from django import forms
from .models import Book
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]


# Example form to demonstrate CSRF protection & secure input handling
class ExampleForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter your name"})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message"})
    )
