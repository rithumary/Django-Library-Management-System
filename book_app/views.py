from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome to Library Management System")
def library(request):
    return HttpResponse("Welcome to Our Library")
def book(request):
    return HttpResponse("Available Books: Python, Django, Java, React, MySQL")
def book_details(request):
    return HttpResponse("Book Name: Django | Author: William S. Vincent")
def contact(request):
    return HttpResponse("Contact us at library@gmail.com")

# Create your views here.
