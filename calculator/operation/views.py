from django.shortcuts import render
from django.views.generic import View
from operation.forms import Formname,Emiform,Sighnup,Signin

# Create your form here.

class FormView(View):
    def get(self,request):
        form=Formname()#eghne kodthal form submit cheyimbo blank avum
        return render(request,"forms.html",{"form":form})
    def post(self,request):
        print(request.POST) # context dic akan
        form=Formname(request.POST)
        if form.is_valid():
            print("myname",form.cleaned_data["name"])
            print("email",form.cleaned_data["email"])
            print("address",form.cleaned_data["address"])
            print("password",form.cleaned_data["password"])
            print("phone",form.cleaned_data["phone"])
            form=Formname()#eghne kodthal form submit cheyimbo blank avum  
        else:
            print("good byy")
        return render(request,"forms.html",{"form":form})

class Emiview(View):
    def get(self,request):
        form=Emiform()
        return render(request,"emi.html",{"form":form})
    def post(self,request):
        print(request.POST)
        form=Emiform(request.POST)
        if form.is_valid():
            # print("loan_amount",form.cleaned_data["loan_amount"])
            # print("tenure",form.cleaned_data["tenure"])
            # print("interest",form.cleaned_data["interest"])
            

            # OR
            
            print(form.cleaned_data)
            loan_amount=form.cleaned_data.get('loan_amount')
            tenure=form.cleaned_data.get('tenure') # values get cheyan vendi
            interest=form.cleaned_data.get('interest')
            form=Emiform()
            n=tenure*12
            r=interest
            p=loan_amount
            emi=p*r*(1+r)**n/((1+r)**n-1)
            print(emi)
        else:
            print("invalid data")
        return render(request,"emi.html",{"form":form})
    
class Sighnview(View):
    def get(self,request):
        form=Sighnup()
        return render(request,"sighnup.html",{"form":form})
    def post(self,request):
        form=Sighnup(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data["email"])
            print(form.cleaned_data)
            #or
            # p=form.cleaned_data.get("password")
            form=Sighnup()
        else:
            print("invalid")
        return render(request,"sighnup.html",{"form":form})

# check password is match or no

class sighnview(View):
    def get(self, request):
        form = Signin()
        return render(request, "sighin.html", {"form": form}) 

    def post(self, request):
        form = Signin(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("Username")
            email = form.cleaned_data.get("email")
            password1 = form.cleaned_data.get("password")
            password2 = form.cleaned_data.get("confirm_password")
            
            if password1 == password2:
                print(form.cleaned_data)
                form = Signin()
            else:
                print("Passwords do not match!!!!")    
        else:
            print("Form is invalid")

        return render(request, "sighin.html", {"form": form})

#OR

# class sighnview(View):
#     def get(self,request):
#         form=Signin()
#         return render(request,"sighin.html",{"form":form})
#     def post(self,request):
#         form=Signin(request.POST)
#         if form.is_valid(): 
#             if form.cleaned_data.get('password')==form.cleaned_data.get("confirm_password"):
#                 print(form.cleaned_data)
#                 form=Signin()
#             else:
#                 print("password not match..")
            
#         else:
#             print("invald input..!")

#         return render(request,"sighin.html",{"form":form})
    


    





# create views

class HelloworldView(View): 
    def get(self,request):
        return render(request,"Helloworld.html")
    
class HelloView(View):
    def get(self,request):
        return render(request,"Hello.html")
    
class newView(View):
    def get(self,request):
        return render(request,"View.html")

class add(View):
    def get(self,request):
        return render(request,"add.html")
    def post(self,request):
        print(request.POST) #dic variable name(request.post)
        request.POST.get("num1","num2")
        n1= int(request.POST["num1"])
        n2= int(request.POST["num2"])
        result= n1+n2
        print(result)
        return render(request,"add.html",{"res":result})
    
class subview(View):
    def get(self,request):
        return render(request,"sub.html")
    def post(self,request):
        print(request.POST) #dic variable name(request.post)
        request.POST.get("num1","num2")
        n1= int(request.POST["num1"])
        n2= int(request.POST["num2"])
        result= n1-n2
        print(result)
        return render(request,"sub.html",{"res":result})  

class mulview(View):
    def get(self,request):
        return render(request,"mul.html")
    def post(self,request):
        print(request.POST) 
        request.POST.get("num1","num2")
        n1= int(request.POST["num1"])
        n2= int(request.POST["num2"])
        result= n1*n2
        print(result)
        return render(request,"mul.html",{"res":result})

class divview(View):
    def get(self,request):
        return render(request,"div.html")
    
    def post(self,request):
        print(request.POST) 
        request.POST.get("num1","num2")
        n1= int(request.POST["num1"])
        n2= int(request.POST["num2"])
        result= n1/n2
        print(result)
        return render(request,"div.html",{"res":result})  
    
class oddeven(View):
    def get(self,request):
        return render(request,"oddeven.html")
    def post(self,request):
        request.POST.get("number")
        num=int(request.POST["number"])
        if num%2==0:
            res="even"
        else:
            res="odd"
        return render(request,"oddeven.html",{"result":res})

class leapyear(View):
    def get(self,request):
        return render(request,"leap.html")
    def post(self,request):
        request.POST.get("year")
        year=int(request.POST["year"])
        if year%400==0 and year%100==0:
            res="leap year"
        elif year%4==0 and year%100!=0:
            res="leap year"
        else:
            res="not leap year"
        return render(request,"leap.html",{"result":res})

class armstrong(View):
    def get(self,request):
        return render(request,"arms.html")
    def post(self,request):
        request.POST.get("num")
        num=int(request.POST["num"])
        sum=0
        temp=num
        while temp>0:
            digit=temp%10
            sum+=digit**3
            temp//=10
            if(num==sum):
                res="Armstrong"
            else:
                res="Not Armstrong"
        return render(request,"arms.html",{"result":res})
    
class largest(View):
    def get(self,request):
        return render(request,"large.html")

    def post(self,request):
        request.POST.get("num1","num2")
        n1=int(request.POST["num1"])
        n2=int(request.POST["num2"])
        if n1>n2:
            res=n1,"number1 is larger"
        else:
            res=n2,"number2 is  larger"
        return render(request,"large.html",{"result":res})
    
class palindrome(View):
    def get(self,request):
        return render(request,"palin.html")
    def post(self,request):
        request.POST.get("num")
        num=int(request.POST["num"])
        rev=0
        temp=num
        while temp>0:
            digit=temp%10
            rev=rev*10+digit
            temp//=10
            if(num==rev):
                res="palindrome"
            else:
                res="not palindrome"
        return render(request,"palin.html",{"result":res})
    
class palindromes(View):
    def get(self,request):
        return render(request,"palins.html")
    def post(self,request):
        request.POST.get("string")
        str=(request.POST["string"])
        s=str[::-1]
        if s==str:
           res="palindrome"
        else:
            res="not palindrome"
        return render(request,"palins.html",{"result":res})

class new(View):
    def get(self,request):
        return render(request,"new.html")
    def post(self,request):
        request.POST.get("string")
        str=(request.POST["string"])
        string="{()}"
        if string==str:
            res="valid"
        else:
            res="invalid"
        
        return render(request,"new.html",{"result":res})
    
class greeting(View):
    def get(self,request):
        return render(request,"greeting.html")
    def post(self,request):
        request.POST.get("name")
        str=(request.POST["name"])
        res=f"hello {str} welcome to luminar"
        return render(request,"greeting.html",{"result":res})


class prime(View):
    def get(self,request):
        return render(request,"prime.html")
    def post(self,request):
        request.POST.get("number")
        num=int(request.POST["number"])
        if num==1:
            res="num is not a prime number"
        elif num==2:
            res="2 is a prime number"
        else:
            for i in range(2,num):
                if num%i==0:
                    res="not prime"
                    break
                else:
                    res="prime"        
        return render(request,"prime.html",{"result":res})

class fibanocci(View):
    def get(self,request):
        return render(request,"fib.html")
    def post(self,request):
        request.POST.get("number")
        num=int(request.POST["number"])
        n1=0
        n2=1
        count=0
        res=""
        if num<=0:
            res="The fibannoci series is"
        elif num==1: 
            res=f"{n1}"
        else:
            while count<num:
                res+=f"{n1} "
                n3=n1+n2
                n1=n2
                n2=n3
                count+=1
        return render(request,"fib.html",{"result":res})

