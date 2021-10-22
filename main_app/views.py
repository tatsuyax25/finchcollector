from django.shortcuts import render, redirect
# render in django renders template
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Toy
# Import the FeedingForm
from .forms import FeedingForm

# Add the following import
from django.http import HttpResponse

# Create your views here.
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


# Define the home view
def home(request):
    return render(request, 'home.html')
    
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

    #Get the toys the Finch doesn't have!
    toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toys.all().values_list('id'))
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        # include the finch and feeding_form in the context
        'finch': finch, 'feeding_form': feeding_form, 'toys': toys_finch_doesnt_have
    })

def assoc_toy(request, finch_id, toy_id):
    # Note that you cacn pass a toy's id instead of the whole object
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)

def add_feeding(request, finch_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db unitl it
        #has the finch_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)


