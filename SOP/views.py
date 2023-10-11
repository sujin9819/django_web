from django.shortcuts import render

def Protocol(request):
    return render(request, 'SOP/PROTOCOL.html')
def Protocol_list(request):
    return render(request, 'SOP/Protocol_list.html')
#리스트의 경우 SOP 목록을 DB화해서 활용