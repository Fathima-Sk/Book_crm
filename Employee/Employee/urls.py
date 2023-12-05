"""
URL configuration for Employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Work.views import Empview,bookview,booklist,book_details_view,book_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',Empview.as_view()),
    path('book/',bookview.as_view()),
    path('books/all',booklist.as_view(),name="book-al"),
    path('bookv/<int:pk>',book_details_view.as_view(),name="book-det"),
    path('bookv/<int:pk>/remove',book_delete.as_view(),name="book-del"),
]
