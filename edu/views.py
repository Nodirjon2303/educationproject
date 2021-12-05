import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
import json

def index_view(request):
    cources = Courses.objects.all()
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        user = request.user
        user.__dict__.update({f"{data['name']}": data['value']})
        print(user.first_name)
        user.save()

        return  JsonResponse({'data': 'ok'})

    return render(request, 'index.html', {'cources': cources})


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
    return  render(request, 'user page.html', {})