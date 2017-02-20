from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    context = {
    'courses' : Course.objects.all()
    #select * from Blog
    }
    return render(request, "my_courses/index.html", context)

def course(request):
    Course.objects.create(course_name = request.POST['course_name'], description = request.POST['description'])
    return redirect('/')
