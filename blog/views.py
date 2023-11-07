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
    search_type = request.GET.get('search_type')
    search_keyword = request.GET.get('search_keyword')
    if search_keyword is None:
        search_keyword = ""

    if len(search_keyword) > 0:
        if search_type == '1':
            log_list = MAGdata.objects.order_by('pk').filter(Taxon__contains=search_keyword)
        elif search_type == '2':
            log_list = MAGdata.objects.order_by('pk').filter(MAG_index__contains=search_keyword)
    else:
        search_type = '1'
        search_keyword = ''
        log_list = MAGdata.objects.all()

    paginator = Paginator(log_list, 15) 
    page = request.GET.get('page')
    magdatas = paginator.get_page(page)
    return render(request, 'blog/Genome.html',{'magdatas': magdatas, 'type': search_type, 'keyword': search_keyword})

def MAG_detail(request, pk):
    MAGdetail = MAGdata.objects.get(pk=pk)
    total_gene = GeneData.objects.filter(MAG=MAGdetail.pk)
    gene_count = total_gene.count()
    search_type = request.GET.get('search_type')
    search_keyword = request.GET.get('search_keyword') 
    if search_keyword is None:
        search_keyword = ""
    if len(search_keyword) > 0:
        if search_type == '1':
            log_list = GeneData.objects.order_by('pk').filter(Gene_description__contains=search_keyword,MAG=MAGdetail.pk)
        elif search_type == '2':
            log_list = GeneData.objects.order_by('pk').filter(Gene_symbol__contains=search_keyword,MAG=MAGdetail.pk)
    else:
        search_type = '1'
        search_keyword = ''
        log_list = GeneData.objects.filter(MAG=MAGdetail.pk)
    paginator = Paginator(log_list, 15) 
    page = request.GET.get('page')
    genes = paginator.get_page(page)
    return render(request, 'blog/MAG_detail.html', {'MAGdetail': MAGdetail,'genes':genes,'gene_count':gene_count,'type': search_type, 'keyword': search_keyword})

def Samples(request):
    sampledatas = sample.objects.all().order_by('sample_ID')
    return render(request, 'blog/Samples.html',{'sampledatas':sampledatas})

def search(request):
    search_type = request.GET.get('search_type')
    searched = request.GET.get('searched')     
    if len(searched) > 0:
        if search_type == '1':
            genes = GeneData.objects.filter(Gene_description__contains=searched).order_by('-RNAcount','-Ribocount')
        elif search_type == '2':
            genes = GeneData.objects.filter(Gene_symbol__contains=searched).order_by('-RNAcount','-Ribocount')
        gene_count = genes.count()
        paginator = Paginator(genes, 25) 
        page = request.GET.get('page')
        genes = paginator.get_page(page)
        return render(request, 'blog/gene_search.html', {'searched': searched, 'genes': genes,'gene_count':gene_count,'type': search_type})
    else:
        return render(request, 'blog/gene_search.html', {})

        
 