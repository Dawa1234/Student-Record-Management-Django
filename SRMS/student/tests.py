from django.urls import reverse 
from django.test import TestCase , SimpleTestCase ,Client
from .views import studentlist , studentUpdate
from django.contrib.auth.models import User

# Create your tests here.

class TestViews(TestCase):

    def test_std_list(self):

        # Only creates user object for test case.
        user = User.objects.create(username= 'testcase')
        user.set_password('123456')
        user.save()

        # Fetching all the functions from client() method.
        client = Client()

        # For log_in, else will redirect and fail the test
        logged_in = client.login(username='testcase' , password = '123456')

        # Get function urls
        url = reverse('studentlist')

        #  Getting the status_code. (if logged_in; status_code=200, if not(redirected); status_code = 302)
        response = client.get(url)
        
        # Tests 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response , 'student/studentlist.html')