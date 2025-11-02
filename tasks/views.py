from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    # Work With database
    # Transform Data
    # Data Pass
    # HTTP Response / json Response
    return HttpResponse("Welcome to the Task Managment System")


def contact(request):
    return HttpResponse("<h1 style='color: yellow'>This Is Contact Page<h/>")


def show_task(request):
    return HttpResponse("This Is a Task Page")


def show_specific_task(request, id):
    print("id", id)
    print("id Type ", type(id))
    return HttpResponse(f"This Is a Specific taks Page {id}")
