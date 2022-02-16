from django.urls import path
from . import views

urlpatterns = [
    # View Dashboard and admin profile
    path('admin_dashboard' , views.admin_dashboard , name= 'dashboard'),
    path('adminprofile/<int:admin_id>', views.profile),
    path('update/<int:admin_id>', views.update),
    path('adminlist', views.adminlist),

    # Authority to add, delete and update studnets.
    path('addstudent', views.addstudent , name = 'create'),
    path('update_student/<int:std_id>', views.UpdateStudent , name = 'update'),
    path('delete_student/<int:stud_id>', views.deleteStudent , name = 'delete')
]