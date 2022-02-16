from django import forms
from .models import Student

# Add Student Form
class Student_data(forms.ModelForm):
    class Meta():
        model = Student
        fields = "__all__"

