from curses.ascii import HT
from webbrowser import get
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from Admin_panel.models import Student
from Admin_panel.forms import Student_data
from django.contrib.auth.models import User , Group
from account.forms import Registerform

# Create your views here.

# ------------------------------------------ Student dashboard------------------------------------------
@login_required(login_url='/login/login_redirect')
def student_dashboard(request):

    enrolled = Student.objects.count()
    return render(request , 'student/studentpage.html' ,{'enrolled' : enrolled})

# ------------------------------------------Add new student------------------------------------------
@login_required(login_url='/login/login_redirect')
def studentlist(request):
    # Total number of rows
    totat_students = Student.objects.count()

    if(request.method == "POST"):

        if(request.POST.get('showrecords') == "All"):
            all_data = 10000;
            # All the data that are in the student model.
            AllStudents = Student.objects.all().order_by('student_name')[:all_data]

            context = {'studentdata' : AllStudents , 'total_student' : totat_students}
            
            messages.info(request , 'Showing '+request.POST.get('showrecords')+' rows from the Table')
            return render(request , 'student/studentlist.html' , context)
        else:
            # All(all()) selected number of data that are in the student model in alphabetical order (order_by student_name)
            AllStudents = Student.objects.all().order_by('student_name')[:int(request.POST.get('showrecords'))]

            context = {'studentdata' : AllStudents , 'total_student' : totat_students}
            
            messages.info(request , 'Showing '+request.POST.get('showrecords')+' rows from the Table')
            return render(request , 'student/studentlist.html' , context)

    else:
        AllStudents = Student.objects.order_by('student_name')
        # limited_number = Student.objects.get
        context = {'studentdata' : AllStudents , 'total_student' : totat_students}

        messages.info(request , 'Selected 10 rows from Table')
        return render(request , 'student/studentlist.html' , context)



# ------------------------------------------Student with Account ------------------------------------------
@login_required(login_url='/login/login_redirect')
def studentAccProfile(request , std_id):
    student_data = User.objects.get(id = std_id)
    form = Registerform()


    group = Group.objects.get(name = 'student')

    return render(request , 'student/studentaccprofile.html' , {'student_data' :student_data, 'form' : form })


# ------------------------------------------Student without Account ------------------------------------------
@login_required(login_url='/login/login_redirect')
def studentprofile(request, stud_id):
    st_data = Student.objects.get(student_id = stud_id)
    st_form = Student_data()
    return render(request , 'student/studentprofile.html' ,{'student_data' : st_data , 'student_form' : st_form})



# ------------------------------------------Class------------------------------------------
@login_required(login_url='/login/login_redirect')
def studentclass(request):

    # Total number of rows
    std_class = request.POST.get('std_class')
    totat_students = Student.objects.filter(student_class = std_class).count()
    if(request.method == "POST"):

        if(request.POST.get('showrecords') == "All"):
            all_data = 10000;


            # All the data that are in the student model whose class is "std_class" i.e student_class = ?
            AllStudents = Student.objects.filter(student_class = std_class).order_by('student_name')[:all_data]
            
            context = {'studentdata' : AllStudents , 'total_student' : totat_students}
            
            messages.info(request , 'Showing '+request.POST.get('showrecords')+' rows from the Table/Class ' + request.POST.get('std_class'))
            return render(request , 'student/studentclass.html' , context)
        else:
            # All(all()) selected number of data that are in the student model in alphabetical order (order_by student_name)
            AllStudents = Student.objects.filter(student_class = std_class).order_by('student_name')[:int(request.POST.get('showrecords'))]

            context = {'studentdata' : AllStudents , 'total_student' : totat_students}
            
            messages.info(request , 'Showing '+request.POST.get('showrecords')+' rows from the Table/Class ' + request.POST.get('std_class'))
            return render(request , 'student/studentclass.html' , context)



    else:
        AllStudents = Student.objects.all()[:0]
        context = {'studentdata' : AllStudents , 'total_student' : totat_students}


        return render(request , 'student/studentclass.html' , context)

# ------------------------------------------Student Update------------------------------------------
@login_required(login_url='/login/login_redirect')
def studentUpdate(request, std_id):
    std_update = User.objects.get(id = std_id)

    
    if (request.method == "POST"):
        form = Registerform(request.POST,request.FILES , instance= std_update)
        context = {'student_id' : std_id}

        if  (form.is_valid()):

            form.save()
            messages.success(request , 'Profile Successfully Updated!')
            return render(request,'student/studentaccprofile.html', {'student_data' : std_update})

        else:
            messages.error(request , '*Invalid form!*')
            return render(request,'student/studentaccprofile.html', {'student_data' : std_update})
    else:
        return HttpResponse('This is not a POST request!')


