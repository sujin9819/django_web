from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def About(request):
    return render(request, 'blog/About.html')

def Gene(request):
    return render(request, 'blog/Gene.html')

def Genome(request):
    return render(request, 'blog/Genome.html')

def Samples(request):
    return render(request, 'blog/Samples.html')
