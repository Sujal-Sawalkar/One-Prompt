from django.shortcuts import render

def home(request):
    return render(request, 'ai_tools/home.html')

def login(request):
    return render(request, 'ai_tools/login.html')

def signup(request):
    return render(request, 'ai_tools/signup.html')

def logout(request):
    return render(request, 'ai_tools/logout.html')