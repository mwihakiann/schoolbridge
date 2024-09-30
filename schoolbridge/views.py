from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages as django_messages  # Avoid conflict
from .models import Message, Announcement, Task, Grade, File
from .forms import MessageForm, AnnouncementForm, TaskForm, GradeForm, FileUploadForm

# View function to render the tasks/index.html template
def index(request):
    template_name = 'tasks/index.html'
    print(template_name)
    tasks = Task.objects.all()
    
    return render(request, 'template_name', {'tasks': tasks})

@login_required
def index(request):
    """Displays messages based on user role (parent or teacher)"""
    if request.user.is_parent:
        user_messages = Message.objects.filter(recipient=request.user)
    elif request.user.is_teacher:
        user_messages = Message.objects.filter(sender=request.user)
    return render(request, 'index.html', {'messages': user_messages})

@login_required
def message_list(request):
    """Lists all messages for authenticated users"""
    all_messages = Message.objects.all()
    return render(request, 'message_list.html', {'messages': all_messages})

@login_required
def message_detail(request, pk):
    """Displays details of a specific message"""
    message = get_object_or_404(Message, pk=pk)
    return render(request, 'message_detail.html', {'message': message})

@login_required
def announcement_list(request):
    """Lists all announcements"""
    announcements = Announcement.objects.all()
    return render(request, 'announcement_list.html', {'announcements': announcements})

@login_required
def announcement_detail(request, pk):
    """Displays details of a specific announcement"""
    announcement = get_object_or_404(Announcement, pk=pk)
    return render(request, 'announcement_detail.html', {'announcement': announcement})

# Additional features (implement as needed)
@login_required
def task_list(request):
    """Lists all tasks assigned to the student (user)"""
    if request.user.is_student:
        tasks = Task.objects.filter(student=request.user)
    else:
        tasks = None
        django_messages.warning(request, 'You cannot access the task list.')
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def gradebook(request):
    """Lists all grades for the student (user)"""
    if request.user.is_student:
        grades = Grade.objects.filter(student=request.user)
    else:
        grades = None
        django_messages.warning(request, 'You cannot access the gradebook.')
    return render(request, 'gradebook.html', {'grades': grades})

@login_required
def file_upload(request):
    """Allows upload of files (assuming user is a teacher)"""
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

@login_required
def file_list(request):
    """Lists all uploaded files"""
    files = File.objects.all()
    return render(request, 'file_list.html', {'files': files})

@login_required
def file_detail(request, pk):
    """Displays details of a specific uploaded file"""
    file = get_object_or_404(File, pk=pk)
    return render(request, 'file_detail.html', {'file': file})
