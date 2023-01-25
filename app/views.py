from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.


def first(request):
    a=employee.objects.all()
    d={'emp':a}
    return render(request, 'first.html',d)
def second(request):
    b=dept.objects.all()
    d={'dep':b}
    return render(request, 'second.html',d)