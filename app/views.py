from rest_framework import generics
from .models import User, Authors, Book
from .serializers import *
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView, Response
from django.core.paginator import Paginator
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import views





# class UserCreatePIView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer

class UserProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateProfileSerializer

class UserSecurityUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSecuritySerializer


class AuthorsListAPIView(generics.ListAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsListSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend, ]
    pagination_class = LimitOffsetPagination
    search_fields = ("full_name", )
    filterset_fields = ("period", )
    

class AuthorsCreateAPIView(generics.CreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsCreateSerializer

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend, ]
    pagination_class = LimitOffsetPagination
    search_fields = ("title", )
    filterset_fields = ("author", 'category', )

class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer

class PeriodAPIView(generics.ListAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer

class AuthorsDetailAPIVIew(generics.RetrieveAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsDetailSerializer

class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = UserSerializer
    # permission_classes = None

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(serializer.validated_data['password'])
        user.set_password(serializer.validated_data['password'])
        return Response({
            "user":serializer.data,
            'tokens': user.get_token()
        })
    


class UserAPIView(views.APIView):


    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(email=serializer.validated_data.get('email'))
        return Response({
            'tokens': user.get_token()
        }, status=status.HTTP_200_OK)