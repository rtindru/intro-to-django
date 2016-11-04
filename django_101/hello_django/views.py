from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_django(request):
    return HttpResponse('Hello Django!')


def hello_user(request, user):
    return HttpResponse('Hello ' + user + '!')


def hello_template(request, user):
    return render(request, 'hello.html', {'user': user})


def hello_template_two(request, user):
    return render(request, 'hello_two.html', {'user': user})

