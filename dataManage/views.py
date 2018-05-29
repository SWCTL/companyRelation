from django.shortcuts import render
from django.shortcuts import HttpResponse
from dataManage import models

# Create your views here.

def index(request):
    return render(request, "index.html")


def result(request):
    return render(request, "result.html")

def fail(request):
    return render(request, "fail.html")

def search(request):
    com_name = request.GET.get('com_name')
    error_msg = ''
    company = models.TCorp.objects.get(corp_name=com_name)

    if not com_name:
        error_msg = '请输入关键词'
        return render(request, 'fail.html', {'error_msg': error_msg})

    return render(request, "result.html", {'company': company})