from rest_framework import viewsets
from . import models
from . import serializers

class WriterViewset(viewsets.ModelViewSet):
    queryset = models.Writer.objects.all()
    serializer_class = serializers.WriterSerializer

class BookViewset(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer