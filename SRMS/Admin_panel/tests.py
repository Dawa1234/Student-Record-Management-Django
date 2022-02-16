from django.urls import reverse , resolve
from django.test import TestCase , SimpleTestCase , Client
from .views import admin_dashboard, addstudent , UpdateStudent , deleteStudent
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Student

# Create your tests here.
class TestUrls(SimpleTestCase):
    # Testing urls
    def test_admin_dashoboard_url(self):
        url = reverse('dashboard')

        self.assertEqual(resolve(url).func , admin_dashboard)
    
    # Create
    def test_craete_url(self):
        url = reverse('create')

        self.assertEqual(resolve(url).func , addstudent)


    # Update
    def test_update_url(self):
        url = reverse('update' , args=[1])

        self.assertEqual(resolve(url).func , UpdateStudent)


    # Delete
    def test_delete_url(self):
        url = reverse('delete' , args=[1])

        self.assertEqual(resolve(url).func , deleteStudent)

# -------------------------------For testing Views functions -------------------------------
class TestViews(TestCase):

# ------------------------------ Create -----------------------------------
    def test_addstudent(self):

        # Only creates user object for test case.
        user = User.objects.create(username= 'testcase')
        user.set_password('123456')
        user.save()

        # Create group object.
        group = Group.objects.create(name = 'admin')
        admin_side = Group.objects.get(name='admin')

        user.groups.add(admin_side)

        # Fetching all the functions from client() method.
        client = Client()

        # For log_in, else will redirect and fail the test
        logged_in = client.login(username='testcase' , password = '123456')

        # Get function urls
        url = reverse('create')

        #  Getting the status_code. (if logged_in; status_code=200, if not(redirected); status_code = 302)
        response = client.post(url,{
            'student_name': 'test name',
            'student_address': 'test address',
            'student_gender' : 'Male',
            'student_age' :  '1',
            'student_email' :  'test@gmail.com',
            'student_phone' :  'test phone',
            'student_class' :  '2',
            'addmission_date' : 'test date',
            'student_image' : 'test image'
        })
        
        # Tests
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response , '/student/student_dashboard')
        self.assertTemplateUsed(response , 'admin/crud_student/addstudent.html')



# ------------------------------ delete -----------------------------------
    def test_deletestudent(self):

        # Only creates user object for test case.
        user = User.objects.create(username= 'testcase')
        user.set_password('123456')
        user.save()

        # Create group object.
        group = Group.objects.create(name = 'admin')
        admin_side = Group.objects.get(name='admin')

        user.groups.add(admin_side)

        # Fetching all the functions from client() method.
        client = Client()

        # For log_in, else will redirect and fail the test
        logged_in = client.login(username='testcase' , password = '123456')


        created_object = Student.objects.create(
            student_name= 'test name',
            student_address= 'test address',
            student_gender = 'Male',
            student_age =  '1',
            student_email =  'test@gmail.com',
            student_phone =  'test phone',
            student_class =  '2',
            addmission_date = 'test date',
            student_image = 'test image'
        )

        print(created_object.student_id)

        # Get function urls
        url = reverse('delete' , args=[2])

        #  Getting the status_code. (if logged_in; status_code=200, if not(redirected); status_code = 302)
        response = client.delete(url)
        
        # Tests
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response , '/student/studentlist')
        # self.assertTemplateUsed(response , 'admin/crud_student/addstudent.html')



# ------------------------------ Update -----------------------------------
    def test_updatestudent(self):

        # Only creates user object for test case.
        user = User.objects.create(username= 'testcase')
        user.set_password('123456')
        user.save()

        # Create group object.
        group = Group.objects.create(name = 'admin')
        admin_side = Group.objects.get(name='admin')

        user.groups.add(admin_side)

        # Fetching all the functions from client() method.
        client = Client()

        # For log_in, else will redirect and fail the test
        logged_in = client.login(username='testcase' , password = '123456')


        created_object = Student.objects.create(
            student_name= 'test name',
            student_address= 'test address',
            student_gender = 'Male',
            student_age =  '1',
            student_email =  'test@gmail.com',
            student_phone =  'test phone',
            student_class =  '2',
            addmission_date = 'test date',
            student_image = 'test image'
        )
        print(created_object.student_id)

        # Get function urls
        url = reverse('update' , args=[3])

        #  Getting the status_code. (if logged_in; status_code=200, if not(redirected); status_code = 302)
        response = client.post(url,{
            'student_name' : 'test name2',
            'student_address':'test address',
            'student_gender' :'Female',
            'student_age' : '2',
            'student_email' : 'test1@gmail.com',
            'student_phone' : 'test phone',
            'student_class' : '1',
            'addmission_date' : 'test date',
            'student_image':'test image'
        })
        
        # Tests
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response , '/student/studentlist')