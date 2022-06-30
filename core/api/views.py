from core.models import Book
from . serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser


class Bookviewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class= BookSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAdminUser]

