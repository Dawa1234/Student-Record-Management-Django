from django.urls import path
from . import views

urlpatterns = [
    # Student dashboard
    path('student_dashboard' , views.student_dashboard),

    # Student list, profile.
    path('studentlist' , views.studentlist , name = 'studentlist'),
    path('studentAccprofile/<int:std_id>' , views.studentAccProfile),
    path('studentprofile/<int:stud_id>' , views.studentprofile),
    path('studentupdate/<int:std_id>' , views.studentUpdate),
    path('studentclass' , views.studentclass),
]