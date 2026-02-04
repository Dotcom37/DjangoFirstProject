

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book , Author , Publisher
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .forms import BookForm, AuthorForm, AuthorFormWithoutAuthor

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

class BookListView(ListView):
    model = Book
    template_name = 'library/cbv_book_list.html'
    context_object_name = 'books'

#function based view for book detail
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})

#class based view for book detail
class BookDetailView(DetailView):
    model= Book
    template_name = 'library/cbv_book_detail.html'
    context_object_name='book'

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})


def book_by_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(authors=author)
    context = {'author': author, 'books': books}
    return render(request, 'library/book_by_author.html', context) 


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # redirect after successful POST
    else:
        form = BookForm()  # GET request → show empty form

    # Always return a response
    return render(request, 'library/add_book.html', {'form': form})

def add_book_and_author(request):
    if request.method == 'POST':
        book_form = AuthorFormWithoutAuthor(request.POST)
        author_form = AuthorForm(request.POST)

        if book_form.is_valid() and author_form.is_valid():
            author = author_form.save()

            book = book_form.save(commit=False)
            book.authors = author
            book.save()

            book_form.instance = book
            book_form.save_m2m()   # ✅ THIS now works

            return redirect('book_list_fbv')

    else:
        book_form = AuthorFormWithoutAuthor()
        author_form = AuthorForm()

    context = {
        'book_form': book_form,
        'author_form': author_form
    }
    return render(request, 'library/add_book_and_author.html', context)
