from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    context = {
    'courses' : Course.objects.all()
    #select * from courses
    }
    return render(request, "my_courses/index.html", context)

def course(request):
    Course.objects.create(course_name = request.POST['course_name'], description = request.POST['description'])
    return redirect('/')

def destroy(request, id):
    context = {
    'courses' : Course.objects.filter(id = id)[0]
    #select just the first index position in a filter.
    }
    print context['courses'].course_name
    return render(request,'my_courses/destroy.html', context)

def delete(request):
    print request.POST['id']
    if request.method == 'POST':
        Course.objects.filter(id = request.POST['id']).delete()
        return redirect('/')
