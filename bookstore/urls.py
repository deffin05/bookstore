"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from auth.views import UserList, UserDetail
from store.views import BookList, AuthorList, PublisherList, BookDetail, AuthorDetail, PublisherDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookList.as_view()),
    path('books/<int:pk>', BookDetail.as_view()),
    path('authors/', AuthorList.as_view()),
    path('authors/<int:pk>', AuthorDetail.as_view()),
    path('publishers/', PublisherList.as_view()),
    path('publishers/<int:pk>', PublisherDetail.as_view()),

    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
