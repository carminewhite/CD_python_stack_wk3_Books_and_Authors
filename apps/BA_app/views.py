from django.shortcuts import render, redirect
from .models import Book, Author

# Home page (defaults to showing all books in the database)
def index(request):
    context = {
        "all_books" : Book.objects.all()
    }
    return render(request, "BA_app/index.html", context)

#authors home page
def authors(request):
    context = {
        "all_authors" : Author.objects.all()
    }
    return render(request, "BA_app/authors.html", context)

#add authors to database
def add_authors(request):
    Author.objects.create(first_name = request.POST["fname"], last_name = request.POST["lname"], notes = request.POST["notes"])
    return redirect('/authors')

#view author details page
def view_author(request, my_id):
    my_author = Author.objects.get(id=my_id)

    context = {
        "this_author" : Author.objects.get(id=my_id),
        "this_authors_books" : my_author.books.all(),
        "all_books" : Book.objects.all(),
    }
    print(context)
    return render(request, "BA_app/view_authors.html", context)

#add a book to the author's listed books they have written, from the dropdown list in view_authors.html
def add_book_to_author(request):
    page_author = Author.objects.get(id=request.POST['page_author'])
    page_author_id = request.POST['page_author']
    book_id = request.POST["books"]
    page_author.books.add(Book.objects.get(id=book_id))

    return redirect(f"/view_author/{page_author_id}")



#view specific book page
def books(request, my_id):
    my_book = Book.objects.get(id=my_id)

    context = {
        "this_book" : Book.objects.get(id=my_id),
        "this_book_authors" : my_book.authors.all(),
        "all_authors" : Author.objects.all(),
    }
    print(context)
    return render(request, "BA_app/books.html", context)

#add a new book to the database
def add_book(request):
    Book.objects.create(title = request.POST["title"], desc = request.POST["description"])
    return redirect("/")

#delete a book from the database
def del_book(request):
    c = Book.objects.get(id = request.POST['del_id'])
    c.delete()
    return redirect("/")

#add an author to the book you are looking at, from the dropdown list in view_authors.html
def add_author_to_book(request):
    page_book = Book.objects.get(id=request.POST['page_book'])
    page_book_id = request.POST['page_book']
    author_id = request.POST["authors"]
    page_book.authors.add(Author.objects.get(id=author_id))

    return redirect(f"/books/{page_book_id}")
