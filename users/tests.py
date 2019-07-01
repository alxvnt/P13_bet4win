from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User


class IndexPageTest(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('connection'))
        self.assertEqual(response.status_code, 200)


class LoginTestCase(TestCase):

    def test_register(self):
        data = {"username": "test", "mail": "fake@gmail.com", "password": "123456",
                "first_name": "Jogn", "last_name": "smith"
                }

        response = self.client.post(reverse("register"), data=data, follow=True,
                                    HTTP_X_REQUESTED='XMLHttpRequest')
        self.assertTrue(response.status_code, 200)
        fake_user = User.objects.create_user(username="test", email="fake@gmail.com", password="123456")

        self.assertTrue(fake_user.username, "test")

    def test_missing_username(self):

        data = {"mail": "fake@gmail.com", "password": "123456",
                "first_name": "Jogn", "last_name": "smith"
                }

        response = self.client.post(reverse("register"), data=data, follow=True,
                                    HTTP_X_REQUESTED='XMLHttpRequest')
        self.assertTrue(response.status_code, 200)
        try:
            User.objects.create_user(username=None, email="fake@gmail.com", password="123456")
        except ValueError:
            self.assertEqual(True, True)
        except:
            self.assertEqual(True, False)

    def test_missing_password(self):

        data = {"username": "test", "mail": "fake@gmail.com",
                "first_name": "Jogn", "last_name": "smith"
                }

        response = self.client.post(reverse("register"), data=data, follow=True,
                                    HTTP_X_REQUESTED='XMLHttpRequest')
        self.assertTrue(response.status_code, 200)
        try:
            User.objects.create_user(username="test", email="fake@gmail.com", password=None)
        except ValueError:
            self.assertEqual(True, True)
        except:
            self.assertEqual(True, False)
