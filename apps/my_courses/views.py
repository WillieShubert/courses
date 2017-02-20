from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    context = {
    'courses' : Course.objects.all()
    #select * from course
    }
    return render(request, "my_courses/index.html", context)

def course(request):
    Course.objects.create(course_name = request.POST['course_name'], description = request.POST['description'])
    return redirect('/')

def destroy(request, id):
    context = {
    'courses' : Course.objects.filter(id = id)
    #select
    }
    return render(request,'my_courses/destroy.html', context)

def delete(request, id):
    if request.method == ['POST']:
        if request.POST['submit'] == ["delete"]:
            Course.objects.filter(id = id).delete()
            return redirect('/')
        elif request.POST['sumbit'] == ["no"]:
            return redirect('/')
