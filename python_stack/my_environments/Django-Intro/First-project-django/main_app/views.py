from django.shortcuts import render, HttpResponse , redirect
from django.http import JsonResponse



def root(request):
    return redirect("/blogs")

def index(request):
    return render(request, "blogs.html")
def new(request):
    return HttpResponse("placeholder  to display a new blog ")

def create(request):
    return redirect('/')

def json(request):
    context = {
        "title": "my first  blog"
        ,
        "content": "this is my first blog"
    }
    return JsonResponse({"response": context,"status": True})  

def show(request, number):
    return HttpResponse(f"placeholder for showing blog number {number}")

def edit(request, number):
    return HttpResponse(f"placeholder for editing blog number {number}")

def destroy(request,number):
    return redirect("/blogs")








