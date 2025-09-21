from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
from django.contrib import messages
from Base import models
from Base.models import Contact

# def home(request):
#    return render(request,'home1.html')
def contact(request):
   if request.method=="POST":
      name=request.POST.get('name')
      email=request.POST.get('email')
      content=request.POST.get('content')
      number=request.POST.get('number')
      print(name,email,number,content)
      if len(name)>1 and len(name)<30:
         pass
      else:
         messages.error(request,'Length of name should be greater than 2 and 30')
         return  render(request,'home.html')
      if len(email)>1 and len(email)<30:
         pass
      else:
         messages.error(request,'Length of email should be greater than 2 and 30')
         return  render(request,'home.html')
      if len(number)>2 and len(number)<13:
         pass
      else:
         messages.error(request,'Length of number should be greater than 2 and 30')
         return  render(request,'home.html')
      ins=models.Contact(name=name,email=email,content=content,number=number)
      ins.save()
      messages.success(request,'Thank you for connecting me \\ your message have been saved')
      print('data has been saved to database')
   
   return render(request,'home2.html')





