from django.shortcuts import render
# render in django renders template
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
# Import the FeedingForm
from .forms import FeedingForm

# Add the following import
from django.http import HttpResponse

# Create your views here.
# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    
def about(request):
    return render(request, 'about.html')

def finches_index(request):
    # let tell our model what to do
    # model go find all the finches in the database
    # don't forget to import your model
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        # include the finch and feeding_form in the context
        'finch': finch, 'feeding_form': feeding_form
    })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url ='/finches/'

class FinchUpdate(UpdateView):
    model = Finch
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'
    