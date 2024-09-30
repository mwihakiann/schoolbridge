from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Meta:
        app_label = 'schoolbridge'

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=50)
    

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Announcement(models.Model):
    sender = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

class Grade(models.Model):
    student = models.ForeignKey(User, related_name='grades', on_delete=models.CASCADE)
    subject = models.ForeignKey(Teacher, related_name='subject_grades', on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)  # Adjust based on your grading system
    date_assigned = models.DateField()

class File(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)