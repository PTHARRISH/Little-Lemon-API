from django.db import IntegrityError
from django.http import JsonResponse
# Imports JsonResponse, which is used to return JSON data in HTTP responses.
from .models import Book
# Imports the Book model from the current app's models.py file, 
# allowing the view to interact with the database.
from django.views.decorators.csrf import csrf_exempt 
# Imports the csrf_exempt decorator, which disables CSRF protection for the decorated view.
from django.forms.models import model_to_dict
from django.shortcuts import render 
# helper functions for rendering templates
from rest_framework import generics
# Imports the generics module from the Django REST framework,
from .serializers import BookSerializer
# Imports the BookSerializer class from the serializers.py file in the current app,
from rest_framework.decorators import api_view
# Imports the api_view decorator from the Django REST framework,


@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({"books":list(books)})
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        book = Book(
            title = title,
            author = author,
            price = price
        )
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)

        return JsonResponse(model_to_dict(book), status=201)
    

# The request parameter contains all the HTTP request data.
# The books view function handles GET and POST requests to the /api/books endpoint.
# request.method-Accesses the HTTP method used in the request.
# GET requests return a JSON response with all books in the database.
# POST requests create a new book record based on the provided data.
 
# request.method == 'GET'-Checks if the request method is GET.
# all()-Queries the database to retrieve all records in the Book table.
# values()- Returns a QuerySet that returns dictionaries instead of model instances.
# list(books)-Converts the QuerySet to a list of dictionaries.
# JsonResponse-Returns a JSON response with the list of books under the key 'books'.

# request.method == 'POST'-Checks if the request method is POST.
# request.POST.get()-Retrieves data from the request's POST parameters.
# model_to_dict(book):
# Converts the Book object into a dictionary for JSON serialization.
# Includes all fields and their values.
# book.save()-Saves the new book record to the database.
# IntegrityError-Occurs when a database constraint is violated.
# status-Indicates the status code of the response.
# 400-Bad Request status code.
# 201-Created status code.
# If a required field is missing, the view returns a 400 Bad Request response.
# model_to_dict(book):
# Converts the Book object into a dictionary for JSON serialization.
# Includes all fields and their values.


class BookView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer 

# The BookView class is a generic view that handles GET and POST requests to the /api/books endpoint.
# The ListCreateAPIView class provides the basic behavior for listing and creating objects.
# queryset-Defines the queryset used to retrieve objects from the database.
# serializer_class-Defines the serializer class used to serialize and deserialize objects.
# The BookSerializer class is used to serialize and deserialize Book objects.
# The view inherits from ListCreateAPIView, which provides the necessary functionality for listing and creating objects.


class SingleBookView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# The SingleBookView class is a generic view that handles GET, PUT, and DELETE requests for a single book.
# The RetrieveUpdateAPIView class provides the basic behavior for retrieving, updating, and deleting objects.
# queryset-Defines the queryset used to retrieve objects from the database.
# serializer_class-Defines the serializer class used to serialize and deserialize objects.
# The view inherits from RetrieveUpdateAPIView, which provides the necessary functionality for retrieving, updating, and deleting objects.
# The view retrieves, updates, or deletes a single book object based on the primary key (pk) provided in the URL.


