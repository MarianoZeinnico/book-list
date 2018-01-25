# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
# -*- coding: utf-8 -*-


# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm
from django.shortcuts import render
from BookList.models import Book
import sqlite3


# Create your views here.

def get(request):
    conn = sqlite3.connect('C:/Users/zeinnico/PycharmProjects/book/db.sqlite3')
        #cursor = conn.cursor()
        #cursor.execute('SELECT * FROM book_list')
        #names = [row[0] for row in cursor.fetchall()]
    showBooksData = Book.objects.all()
    conn.close()
    return render(request, 'Books.html', {'showBooksData': showBooksData})

class Form(ModelForm):
    class Meta:
        model=Book
        fields = ['idBook', 'title', 'author', 'datePublished', 'numberOfPages', 'typeOfBook']

class BookInsert(CreateView):
    model = Book
    success_url = reverse_lazy('book_list')
    fields = ['idBook', 'title', 'author', 'datePublished','numberOfPages', 'typeOfBook']

class BookUpdate(UpdateView):
    model = Book
    success_url = reverse_lazy('book_list')
    fields = ['idBook', 'title', 'author', 'datePublished', 'numberOfPages', 'typeOfBook']

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')

