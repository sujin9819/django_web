import requests
import markdown2
from django.shortcuts import render, HttpResponse
from .models import SOP_list

def Protocol(request):
    return render(request, 'SOP/PROTOCOL.html')
def Protocol_ko(request):
    return render(request, 'SOP/PROTOCOL_ko.html')



def sop_detail_ko(request, sop, title):
    sop_obj = SOP_list.objects.get(SOP=sop, title=title)
    github_url = sop_obj.md_path
    response = requests.get(github_url)
    markdown_text = response.text
    html_content = markdown2.markdown(markdown_text)
    return render(request, 'SOP/Protocol_list_ko.html',{'sop_obj':sop_obj, 'html_content':html_content })

def sop_detail(request, sop, title):
    try:
        sop_obj = SOP_list.objects.get( SOP=sop, title=title)
    except SOP_list.DoesNotExist:
        # 처리할 예외 처리 코드를 여기에 추가
        return HttpResponse("SOP not found", status=404)
    return render(request, 'SOP/Protocol_list.html',{'sop_obj':sop_obj})
