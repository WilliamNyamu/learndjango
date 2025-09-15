from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to my Book Store!</h1>")

def book_view(request):
    return HttpResponse("<h3>You are viewing the book_view View</h3>")

def book_detail(request):
    return HttpResponse("Book detail view successfully done")