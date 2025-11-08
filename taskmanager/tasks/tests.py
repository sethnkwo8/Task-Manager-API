from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from tasks.models import Task

User = get_user_model()

# Create your tests here.
class BaseAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

class TaskAPITestCase(BaseAPITestCase):
    def setUp(self):
        super().setUp()
        self.task = Task.objects.create(user=self.user,
                                        title='Complete test',
                                        description = 'Test out tests',
                                        priority='high',
                                        completed=False)
        self.task_url= reverse('tasks:tasks-list')
        self.detail_url= reverse('tasks:tasks-detail', kwargs={'pk':self.task.id})
        self.task_data = {'title': 'test2', 'description':'Sample data', 'priority': 'low', 'completed': True}

    def test_get_tasks(self):
        response = self.client.get(self.task_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_task(self):
        response = self.client.post(self.task_url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'test2')

    def test_retrieve_task(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Complete test')

    def test_put_task(self):
        response = self.client.put(self.detail_url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'test2')

    def test_delete_task(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthorized(self):
        self.client.credentials()
        response = self.client.get(self.task_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

