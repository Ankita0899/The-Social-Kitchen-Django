from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from home.models import Work

# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
    context = {
        'variable1': "Ankita",
        'variable2': "Srivastava"
    }
    return render(request, 'index.html', context)

def home(request):
  # return HttpResponse("this is about page")
  return render(request, 'home.html',)


def about(request):
  # return HttpResponse("this is about page")
  return render(request, 'about.html',)

def menu(request):
  # return HttpResponse("this is menu page")
  return render(request, 'menu.html',)

def gallery(request):
  # return HttpResponse("this is gallery page")
  return render(request, 'gallery.html',)

def catering(request):
  # return HttpResponse("this is catering page")
  return render(request, 'catering.html',)  

# def work(request):
#   # return HttpResponse("this is work with us page")
#   return render(request, 'work.html',)

def contact(request):
  # return HttpResponse("this is contact page")
   if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      desc = request.POST.get('desc')
      contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
      contact.save()
   return render(request, 'contact.html',)

def work(request):
  # return HttpResponse("this is work page")
   if request.method == "POST":
      fname = request.POST.get('fname')
      lname = request.POST.get('lname')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      resume = request.POST.get('resume')
      add = request.POST.get('add')
      work = Work(fname=fname, lname=lname, email=email, phone=phone, resume=resume, add=add, date = datetime.today())
      work.save()
   return render(request, 'work.html',)