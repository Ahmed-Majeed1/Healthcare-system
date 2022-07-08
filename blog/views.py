from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def doctors(request):
    return render(request, 'blog/doctors.html')

def contact(request):
    return render(request, 'blog/contact.html')
