from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import TaskView

app_name = 'tasks'

router = DefaultRouter()
router.register('tasks', TaskView, basename='tasks')

urlpatterns = [
    path('', include(router.urls))
]