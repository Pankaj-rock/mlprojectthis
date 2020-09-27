from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {'titles': 'django'})
def expresion(request):
    a = request.POST['text1']
    return render(request, 'index.html', {'result': 'pankajkumar'})