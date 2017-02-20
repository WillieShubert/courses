from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "my_courses/index.html")

def course(request):
    Course.objects.create(course_name= request.POST['cou'])
