import json

from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
import json

def index_view(request):
    blogs = Blog.objects.all()
    cources = Courses.objects.all()
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        user = request.user
        student = Student.objects.get(user=user)
        if data['value']:
            student.__dict__.update({f"{data['name']}": data['value']})
            print(student)
            student.save()
            return JsonResponse({'data': 'ok'})
        return JsonResponse({'data': 'error'})

    return render(request, 'index.html', {'cources': cources,
                                          'blogs': blogs})


def home_view(request):

    return render(request, 'index.html', {})


def about_view(request):
    return render(request, 'about.html', {})


def coach_view(request):
    return render(request, 'coaching.html', {})


def time_view(request):
    return render(request, 'time.html', {})


def contact_view(request):
    return render(request, 'contact.html', {})


def userpage_view(request):
    student = Student.objects.get(user=request.user)
    return  render(request, 'user page.html', {'student': student})

def courseView(request, id):
    course = Courses.objects.get(id = id)
    course.view+=1
    course.save()

    return render(request, 'Cource details.html', {'course': course})