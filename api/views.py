from rest_framework import generics
from books.models import Book
from .serializer import BookSerializer
from rest_framework.response import Response

class BookAPIView(generics.ListAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer