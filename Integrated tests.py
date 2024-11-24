# نوشتن تست برای کدها
import unittest


class TestFindTwoSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(find_two_sum([2, 7, 11, 15], 9), (2, 7))
        self.assertEqual(find_two_sum([1, 2, 3], 5), (2, 3))
        self.assertIsNone(find_two_sum([1, 2, 3], 7))


if __name__ == '__main__':
    unittest.main()

# تست یکپارچگی
from rest_framework.test import APITestCase


class TaskAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_task(self):
        response = self.client.post('/api/tasks/', {'title': 'New Task'})
        self.assertEqual(response.status_code, 201)

    def test_get_tasks(self):
        self.client.post('/api/tasks/', {'title': 'Task 1'})
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_delete_task(self):
        task = Task.objects.create(user=self.user, title='Task to delete')
        response = self.client.delete(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, 204)
