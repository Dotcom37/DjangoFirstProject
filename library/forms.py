from django  import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'publisher', 'publication_date', 'isbn']

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birth_date']
            
class AuthorFormWithoutAuthor(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['authors']
