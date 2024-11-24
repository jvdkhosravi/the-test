# برای پیاده‌سازی این سیستم، از Django استفاده خواهیم کرد.
# فرض می‌کنیم که یک مدل برای کاربران و وظایف داریم.

# models.py
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)


# views.py
from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        Task.objects.create(user=request.user, title=title)
        return redirect('task_list')
    return render(request, 'add_task.html')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

# معماری ماژولار: از مدل‌ها برای نمایندگی داده، از ویوها برای پردازش درخواست‌ها و از قالب‌ها برای نمایش استفاده می‌شود.
# الگوی طراحی: از الگوی MVC (مدل-نما-کنترل‌گر) استفاده می‌شود، زیرا مدل‌ها، ویوها و کنترلرها به وضوح تفکیک شده‌اند.

------------------------------------------------------------------------------------------------------------------------

# سوال: API ساده برای افزودن، به‌روزرسانی، حذف و خواندن وظایف کاربران.

# views.py
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# serializers.py
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
# مستندات API:
# روش‌ها:
# GET: برای خواندن وظایف.
# POST: برای افزودن وظایف.
# PUT: برای به‌روزرسانی وظایف.
# DELETE: برای حذف وظایف.
# اعتبارسنجی: می‌توان از JWT یا Token Authentication استفاده کرد.
# مدیریت خطا: با استفاده از Django Rest Framework، خطاها به صورت استاندارد مدیریت می‌شوند.