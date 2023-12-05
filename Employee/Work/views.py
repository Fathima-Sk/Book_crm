from django.shortcuts import redirect, render
from django.views.generic import View
from Work.forms import Empform,bookform
from Work.models import Emp,book


# Create your views here.
class Empview(View):
    def get(self,request):
        form=Empform()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        form=Empform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Emp.objects.create(**form.cleaned_data)
            form=Empform()
            return render(request,"add.html",{"form":form})
        else:  
            return render(request,"add.html",{"form":form})
        
# create a book 
    
class bookview(View):
    def get(self,request):
        form=bookform()
        return render(request,"book.html",{"form":form})
    def post(self,request):
        form=bookform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # book.objects.create(**form.cleaned_data)
            form.save()
            form=bookform()
            return render(request,"book.html",{"form":form})
        else:  
            return render(request,"book.html",{"form":form})
        
#fetch all data from db

class booklist(View):
    def get(self,request):
        qs=book.objects.all()
        return render(request,"booklist.html",{"qs":qs})

# fetch details in user specified id
# read a data dynamically

class book_details_view(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        id=kwargs.get("pk") # pk value id assign cheyth(url kodth value)
        qs=book.objects.get(id=id)
        return render(request,"book_view.html",{"qs":qs})

# delete a  data from db

class book_delete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=book.objects.get(id=id).delete()
        return redirect("book-al")








