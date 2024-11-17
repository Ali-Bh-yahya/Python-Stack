from django.shortcuts import *
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        errors = Course.objects.validate(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            description = Description.objects.create(content=request.POST['description'])  # match with the form field
            Course.objects.create(course_name=request.POST['course_name'], description=description)  # match with the form field
            return redirect('/')
    return render(request, 'index.html')

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('index')
    return render(request, 'delete_course.html', {'course': course})