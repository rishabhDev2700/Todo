from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Note


def home(request):
    if request.user.is_authenticated:
        notes = Note.objects.all()
        return render(request, 'home.html', {"notes": notes})
    return redirect('login')


def create_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                        last_name=last_name)
        user.save()
        return redirect('login')
    return render(request, 'create_user.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def add_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        note = Note(title=title, description=description)
        note.save()
        messages.success(request, "Note Added Successfully")
        return redirect('home')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password, request=request)
        login(request, user)
        return redirect('home')
    return render(request, 'login.html')


def delete(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('home')
