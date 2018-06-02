from django.shortcuts import render
from django.http import Http404
from django.shortcuts import HttpResponse
from dataManage import models

# Create your views here.

def index(request):
    corp_names = models.TCorp.objects.values("corp_name")
    return render(request, "index.html", {'corp_names': corp_names})

def result(request):
    return render(request, "result.html")

def fail(request):
    return render(request, "fail.html")

def search(request):
    com_name = request.GET.get('com_name')
    error_msg = ''

    if not com_name:
        error_msg = '请输入关键词'
        return render(request, 'fail.html', {'error_msg': error_msg})

    company = models.TCorp.objects.get(corp_name=com_name)



    return render(request, "result.html", {'company': company})

# def ownershipStucture(company):
#     id = company.id
#     org = company.org
#     seqId = company.seq_id
#     shareholderList = models.TMCorpCorpDist.objects.get(id=id, org=org, seq_id=seqId)
