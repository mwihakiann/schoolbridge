from django import forms
from .models import Message, Announcement, Task, Grade, File

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content']

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['student', 'title', 'description', 'due_date', 'completed']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'grade', 'date_assigned']

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file', 'title', 'description']
