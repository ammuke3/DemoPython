from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
from .models import Team


def home(request):
    obj = Place.objects.all()
    t1 = Team.objects.all()
    return render(request, 'index.html', {'result': obj, 'res': t1})

# def operations(request):
# x = int(request.GET['num1'])
# y = int(request.GET['num2'])
# res = x + y
# mul = x * y
#  div = x / y
# sub = x - y
# return render(request, 'result.html', {'add': res, 'mult': mul, 'division': div, 'subtration': sub})
