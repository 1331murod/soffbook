
from django.urls import path
from .views import *

urlpatterns = [
    #path('users-create/', UserCreatePIView.as_view(), name='user-create'),
    path('users-profile-update/<int:pk>/', UserProfileUpdateAPIView.as_view(), name='user-update-profile'),
    path('users-security-update/<int:pk>/', UserSecurityUpdateAPIView.as_view(), name='user-update-security'),
    path('author-list/', AuthorsListAPIView.as_view(), name='author-list'),
    path('author-create/', AuthorsCreateAPIView.as_view(), name='author-create'),
    path('book-list/', BookListAPIView.as_view(), name='book-list'),
    path('book-create/', BookCreateAPIView.as_view(), name='book-create'),
    path('period-list/', PeriodAPIView.as_view(), name='period-list'),
    path('author-datail/<int:pk>/', AuthorsDetailAPIVIew.as_view(), name='author-detail'),
    path('book-detail/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('signin/', UserAPIView.as_view(), name='signin'),
]