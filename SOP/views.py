import requests
import markdown2
from django.shortcuts import render, HttpResponse
from .models import SOP_list

def Protocol(request):
    return render(request, 'SOP/PROTOCOL.html')
def Protocol_en(request):
    return render(request, 'SOP/PROTOCOL_en.html')



def sop_detail_ko(request, sop, title):
    sop_obj = SOP_list.objects.filter(lang='ko').get(SOP=sop, title=title)
    github_url = sop_obj.md_path
    response = requests.get(github_url)
    markdown_text = response.text
    html_content = markdown2.markdown(markdown_text)
    return render(request, 'SOP/Protocol_list_ko.html',{'sop_obj':sop_obj, 'html_content':html_content })

def sop_detail_en(request, sop, title):
    sop_obj = SOP_list.objects.filter(lang='en').get(SOP=sop, title=title)
    github_url = sop_obj.md_path
    response = requests.get(github_url)
    markdown_text = response.text
    html_content = markdown2.markdown(markdown_text)
    return render(request, 'SOP/Protocol_list.html',{'sop_obj':sop_obj, 'html_content':html_content })
