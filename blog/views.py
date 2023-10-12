from django.shortcuts import render
from .models import MAGdata, sample
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def index(request):
    return render(request, 'blog/index.html')

def About(request):
    return render(request, 'blog/About.html')

def Gene(request):
    return render(request, 'blog/Gene.html')

def Genome(request):
    magdatas = MAGdata.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(magdatas, 15)
    try:
        lines = paginator.page(page)
    except PageNotAnInteger:
        lines = paginator.page(1)
    except EmptyPage:
        lines = paginator.page(paginator.num_pages)
    context = { 'magdatas':lines }
    return render(request, 'blog/Genome.html',context)

def Samples(request):
    sampledatas = sample.objects.all().order_by('sample_ID')
    return render(request, 'blog/Samples.html',{'sampledatas':sampledatas})
