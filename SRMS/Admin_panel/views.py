from django.contrib import messages
from django.forms import forms
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from account.authorization import admin_only
from django.contrib.auth.models import User
from account.forms import Registerform
from .forms import Student_data
from .models import Student

# Create your views here.
# Admin Dashboard
@login_required(login_url='/login/login_redirect')
@admin_only
def admin_dashboard(request):

    # Count Total student in the database.
    enrolled = Student.objects.count()

    return render(request, "admin/dashboard.html" , {'enrolled' : enrolled})


# Admin Profile
@login_required(login_url='/login/login_redirect')
@admin_only
def profile(request, admin_id):
    admin_profile = User.objects.get(id = admin_id)
    form = Registerform()

    context = {"admin_profile": admin_profile , "form" : form}
    return render(request, "admin/adminprofile.html" , context)



# Admin Update Profile
@login_required(login_url='/login/login_redirect')
@admin_only
def update(request, admin_id):
    admin_update = User.objects.get(id = admin_id)

    if (request.method == "POST"):
        form = Registerform(request.POST , instance=admin_update)

        if form.is_valid():
            form.save()
            messages.success(request , 'Profile Successfully Updated!')
            return render(request,'student/adminprofile.html', {'student_data' : admin_update})
        else:
            messages.error(request , '*Invalid form!*')
            return render(request,'student/adminprofile.html', {'student_data' : admin_update})
    else:
        return HttpResponse('No changes!')



# Admin List
@login_required(login_url='/login/login_redirect')
@admin_only
def adminlist(request):
    return render(request , 'admin/adminlist.html')



# Add new student
@login_required(login_url='/login/login_redirect')
@admin_only
def addstudent(request):
    # The form of the model=Student.
    StudentForm = Student_data()

    if (request.method == "POST"):
        StudentForm = Student_data(request.POST, request.FILES)
        if StudentForm.is_valid():
            
            StudentForm.save()
            print('Successfully Added!')
            messages.success(request , 'Successfully admitted!')
            return render(request, 'admin/crud_student/addstudent.html')
        else:
            print('Not added!')
            messages.error(request , 'Please validate following fileds properly!')
            return render(request, 'admin/crud_student/addstudent.html')

    else:
        context = {'studentform' : StudentForm}
        return render(request, 'admin/crud_student/addstudent.html', context )


# Update student
@login_required(login_url='/login/login_redirect')
@admin_only
def UpdateStudent(request, std_id):
    
    update = Student.objects.get(student_id = std_id)
    
    if (request.method == "POST"):
        form = Student_data(request.POST,request.FILES , instance= update)
        if (form.is_valid()):

            form.save()
            print('Successfully updated!')

            messages.success(request ,'Id no. :' + str(std_id) + ' Successfully Updated!')
            return redirect('/student/studentlist')
        else:
            print('Not updated!')
            messages.error(request , 'Please validate!')
            return redirect('/student/studentlist')
    else:
        return HttpResponse('form')


# Update student
@login_required(login_url='/login/login_redirect')
@admin_only
def deleteStudent(request, stud_id):

    deleteAcc = Student.objects.get(student_id = stud_id)
    deleteAcc.delete()
    print('Successfully Deleted!')
    messages.success(request , 'A Profile was successfully deleted!')
    return redirect('/student/studentlist')