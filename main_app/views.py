from django.shortcuts import render
# render in django renders template
from .models import Finch

# Add the following import
from django.http import HttpResponse

# Create your views here.
# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    
def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })