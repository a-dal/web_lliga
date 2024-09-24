from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'standings/home.html')

def tornejos(request):
    return render(request, 'standings/rondes.html')
# Create your views here.
