from django.contrib.auth.models import Group, User
from rest_framework import serializers

from store.models import Book, Author, Publisher


class BookSerializer(serializers.ModelSerializer):
    pages = serializers.IntegerField(min_value=1)
    price = serializers.IntegerField(min_value=1)
    year = serializers.IntegerField(min_value=1900)
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
