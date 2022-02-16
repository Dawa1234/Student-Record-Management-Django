from django.http import HttpResponse
from django.shortcuts import redirect, render

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'student':
            return redirect('/student/student_dashboard')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

        else:
            return redirect('/student/student_dashboard')
            # return render(request, 'error.html')

    return wrapper_function