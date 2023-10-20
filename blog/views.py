from django.shortcuts import render, get_object_or_404
from .models import MAGdata, sample, GeneData
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

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

def MAG_detail(request, pk):
    MAGdetail = MAGdata.objects.get(pk=pk)
    return render(request, 'blog/MAG_detail.html', {'MAGdetail': MAGdetail})

def Samples(request):
    sampledatas = sample.objects.all().order_by('sample_ID')
    return render(request, 'blog/Samples.html',{'sampledatas':sampledatas})

def search(request):
        if request.method == 'POST':
            searched = request.POST['searched']        
            genes = GeneData.objects.filter(Gene_description__contains=searched)
            paginator = Paginator(genes, 25)
            page = request.GET.get('page',1)
            paginated = paginator.get_page(page)
            return render(request, 'blog/gene_search.html', {'searched': searched, 'genes': paginated})
        else:
            return render(request, 'blog/gene_search.html', {})
        
 