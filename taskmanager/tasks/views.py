from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, status
from rest_framework.response import Response
from tasks.models import Task
from tasks.serializers import TaskSerializer, RegisterSerializer

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'message': 'User created successfully. Please log in to get your token.'
        }, status=status.HTTP_201_CREATED)
    
class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Get tasks for logged in user
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


