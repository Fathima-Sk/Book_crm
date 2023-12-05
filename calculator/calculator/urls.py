"""
URL configuration for calculator project.

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
from operation.views import HelloworldView
from operation.views import HelloView,newView,add,subview,mulview,divview,oddeven,leapyear,armstrong,largest,palindrome,palindromes,new,greeting,prime,fibanocci,FormView,Emiview,Sighnview,sighnview

urlpatterns = [
    path('admin/',admin.site.urls),
    path('hello/',HelloworldView.as_view()),
    path('home/',HelloView.as_view()),
    path('view/',newView.as_view()),
    path('addview/',add.as_view()),
    path('sub/',subview.as_view()),
    path('mul/',mulview.as_view()),
    path('div/',divview.as_view()),
    path('num/',oddeven.as_view()),
    path('leap/',leapyear.as_view()),
    path('arm/',armstrong.as_view()),
    path('large/',largest.as_view()),
    path('pali/',palindrome.as_view()),
    path('palis/',palindromes.as_view()),
    path('celi/',new.as_view()),
    path('greet/',greeting.as_view()),
    path('prime/',prime.as_view()),
    path('fib/',fibanocci.as_view()),
    path('form/',FormView.as_view()),
    path('emi/',Emiview.as_view()),
    path('login/',Sighnview.as_view()),
    path('sighin/',sighnview.as_view())
    
]
