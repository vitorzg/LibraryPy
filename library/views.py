from django.shortcuts import render
from .models import Client
from .models import Book

def index(request):
    return render(request,'index.html')

def clientsall(request):
    clients = Client.objects.order_by('name')
    context = {'clients': clients}
    return render(request, 'clients.html', context)

def booksall(request):
    books = Book.objects.order_by('title')
    context = {'books': books}
    return render(request, 'books.html', context)