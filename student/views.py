from django.shortcuts import render
from core.models import Book

# Create your views here.

def Studentdata(request):
    book= Book.objects.all()
    return render(request, 'student/main.html',{'bk':book})