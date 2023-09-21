from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import TodoItem
from .serializers import TodoItemSerializer, UserSerializer
from .forms import TodoItemForm

from django.contrib.auth.models import User
from django.views.generic import ListView

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

def taskView(request):
    tasks = TodoItem.objects.all()
    context = {'tasks': tasks}

    return render(request, 'task.html', context)

def taskCreate(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Task Added successfully!')
    else:
        form = TodoItemForm()
        context = {
            'form': form,
        }
    return render(request, 'new_task.html', context)

# Generic Views for APIView

class TaskListView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

# for the User view

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer