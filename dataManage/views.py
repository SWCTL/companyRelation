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

    # 得到查找的公司
    company = models.TCorp.objects.get(corp_name=com_name)

    # 得到各个股东
    ownertuple = ownershipStucture(company)

    ownerlist = ownertuple[0]              # 股东列表
    maxholder = ownertuple[1].stock_name   # 最大股东
    naturalMan = ownertuple[2].stock_name  # 自然人股东
    enterprise = ownertuple[3].stock_name  # 企业股东

    return render(request, "result.html", {'company': company, 'ownerlist': ownerlist,
                                           'maxholder': maxholder, 'naturalMan': naturalMan,
                                           'enterprise': enterprise})

# 股权结构
def ownershipStucture(company):
    cid = company.id
    corg = company.org
    cseqId = company.seq_id

    # 找出关联表中该公司的股东id
    tempShareholderList = models.TMCorpCorpStock.objects.filter(id=cid, org=corg, seq_id=cseqId)

    # 找出股东表中这些股东的记录
    shareholderList = []
    for e in tempShareholderList:
        shareholderList.append(models.TCorpStock.objects.get(id=e.sub_id, org=e.sub_org, seq_id=e.sub_seq_id))

    # 查找最大股东
    maxcapi = 0
    for e in shareholderList:
        if e.stock_capi > maxcapi:
            maxcapi = e.stock_capi
            maxholder = e

    # 查找自然人股东
    naturalMan = models.TCorpStock.objects.get(stock_type='自然人')

    # 查找企业股东
    enterprise = models.TCorpStock.objects.get(stock_type='企业')

    # 返回股东列表，最大股东，自然人股东，企业股东的tuple
    return shareholderList, maxholder, naturalMan, enterprise
