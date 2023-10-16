from django.shortcuts import render, HttpResponse
from .models import SOP_list

def Protocol(request):
    return render(request, 'SOP/PROTOCOL.html')
def Protocol_list(request):
    return render(request, 'SOP/Protocol_list.html')



def sop_detail(request, lang, sop, title):
    try:
        sop_obj = SOP_list.objects.get(lang=lang, SOP=sop, title=title)
    except SOP_list.DoesNotExist:
        # 처리할 예외 처리 코드를 여기에 추가
        return HttpResponse("SOP not found", status=404)