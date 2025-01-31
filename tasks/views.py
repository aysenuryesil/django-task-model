from django.http import JsonResponse
from django.shortcuts import render, redirect
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from .models import Task
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from .serializers import tasksSerializer


def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, "tasks/create_task.html")

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description', task.description)
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/update_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})


class tasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = tasksSerializer

    @swagger_auto_schema(
        operation_description="Tüm görevleri listeler",
        responses={200: tasksSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        """Bu uç nokta tüm görevleri getirir."""
        return super().list(request, *args, **kwargs)
