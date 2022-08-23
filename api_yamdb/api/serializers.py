from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authentication.models import User
#from reviews.models import Comment, Review


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Недопустимый username "me"')
        return value


class YaMDbTokenObtainPairSerializer(TokenObtainPairSerializer):
    confirmation_code = serializers.CharField()

    def validate_username(self, value):
        get_object_or_404(User, username=value)
        return value

    def validate_confirmation_code(self, value):
        user = self.context['request'].user
        if default_token_generator.check_token(user, value):
            return value
        raise serializers.ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )


class UserDetailSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )


# class CommentSerializer(serializers.ModelSerializer):
#     review = serializers.SlugRelatedField(
#         slug_field='text',
#         read_only=True
#     )
#     author = serializers.SlugRelatedField(
#         slug_field='username',
#         read_only=True
#     )
#
#     class Meta:
#         model = Comment
#         fields = '__all__'
