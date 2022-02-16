from django.urls import resolve , reverse
from django.test import SimpleTestCase , TestCase
from .views import loginfn, register , login
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_register_url(self):
        url = reverse('registration')
        self.assertEqual(resolve(url).func, register)
    
    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, loginfn)

