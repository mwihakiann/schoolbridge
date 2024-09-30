from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Message, Announcement, Task, Grade, File
from .forms import MessageForm, AnnouncementForm, TaskForm, GradeForm, FileUploadForm

# Core functionalities
@login_required
def index(request):
    if request.user.is_parent:
        messages = Message.objects.filter(recipient=request.user)
    elif request.user.is_teacher:
        messages = Message.objects.filter(sender=request.user)
    return render(request, 'index.html', {'messages': messages})

@login_required
def message_list(request):
    messages = Message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})

@login_required
def message_detail(request, pk):
    message = Message.objects.get(pk=pk)
    return render(request, 'message_detail.html', {'message': message})

@login_required
def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcement_list.html', {'announcements': announcements})

@login_required
def announcement_detail(request, pk):
    announcement = Announcement.objects.get(pk=pk)
    return render(request, 'announcement_detail.html', {'announcement': announcement})

# Additional features (implement as needed)
def task_list(request):
    tasks = Task.objects.filter(student=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

def gradebook(request):
    grades = Grade.objects.filter(student=request.user)
    return render(request, 'gradebook.html', {'grades': grades})

def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.teacher = request.user  # Assuming the user is a teacher
            file.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'file_upload.html', {'form': form})

def file_list(request):
    files = File.objects.all()
    return render(request, 'file_list.html', {'files': files})

def file_detail(request, pk):
    file = File.objects.get(pk=pk)
    return render(request, 'file_detail.html', {'file': file})