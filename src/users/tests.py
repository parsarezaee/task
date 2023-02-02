from django.test import TestCase
from django.contrib.auth import get_user_model



class UserManagerTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(first_name="user1", 
                                        last_name="user_last",
                                        email="normal@user.com",
                                        password="foo")
        self.assertEqual(user.first_name, "user1")
        self.assertEqual(user.last_name, "user_last")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(first_name="")
        with self.assertRaises(TypeError):
            User.objects.create_user(last_name="")
        with self.assertRaises(TypeError):    
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(first_name="", last_name="", email="", password="foo")
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(first_name="superuser1",
                                                   last_name="superuser_last",
                                                   email="super@user.com",
                                                   password="foo")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                first_name="superuser1",
                last_name="superuser_last",
                email="super@user.com", 
                password="foo", 
                is_superuser=False
            )
