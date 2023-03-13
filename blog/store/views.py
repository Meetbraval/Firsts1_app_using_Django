from django.shortcuts import render

# Create your views here.


def home(request):
   context = {}
   return render(request, 'store/home.html', context)

def pets(request):
   context = {}
   return render(request, 'store/pets.html', context)

def feature(request):
   context = {}
   return render(request, 'store/feature.html', context)

def contact(request):
   context = {}
   return render(request, 'store/contact.html', context)

def nature(request):
   context = {}
   return render(request, 'store/nature.html', context)

def community(request):
   context = {}
   return render(request, 'store/community.html', context)


