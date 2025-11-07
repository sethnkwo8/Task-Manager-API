from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import TaskView

app_name = 'tasks'

router = DefaultRouter()
router.register('tasks', TaskView.as_view(), basename='tasks')

url_patterns = [
    path('', include(router.urls))
]