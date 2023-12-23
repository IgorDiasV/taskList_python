from django.shortcuts import render, redirect

def home(request):
    return render(request, "main.html")

def addTask(request):
    return redirect("home")