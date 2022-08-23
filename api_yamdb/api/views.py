from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.models import User
from .serializers import (SignUpSerializer, YaMDbTokenObtainPairSerializer,
                          UserDetailSerializer, UserSerializer)
from .permissions import IsSuperUserOrAdmin


class SignUpAPI(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_mail(
                'Код доступа',
                f'Ваш код доступа: {default_token_generator.make_token(user)}',
                'from@api_yamdb.com',
                [serializer.validated_data.get('email')],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class YaMDbTokenObtainPairView(TokenObtainPairView):
    serializer_class = YaMDbTokenObtainPairSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        username = request.user.username
        user = User.objects.get(username=username)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        username = request.user.username
        user = User.objects.get(username=username)
        serializer = UserDetailSerializer(
            user, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsSuperUserOrAdmin,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ('=username',)
