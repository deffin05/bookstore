from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False, max_length=100)
    last_name = serializers.CharField(required=False, max_length=100)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())],
                                   max_length=100)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, min_length=8, max_length=32)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
