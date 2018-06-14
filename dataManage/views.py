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

    # 得到股权结构信息
    structuredic = ownershipStucture(company)

    ownerlist = structuredic['shareholderList']              # 股东列表
    maxholder = structuredic['maxholder'].stock_name         # 最大股东
    naturalMan = structuredic['naturalMan'].stock_name       # 自然人股东
    enterprise = structuredic['enterprise'].stock_name       # 企业股东

    return render(request, "result.html", {'company': company, 'ownerlist': ownerlist,
                                           'maxholder': maxholder, 'naturalMan': naturalMan,
                                           'enterprise': enterprise})

# 股权结构
def ownershipStucture(company):
    cid = company.id
    corg = company.org
    cseqId = company.seq_id

    # 股权结构字典
    stucture = {
        'shareholderList': [],  # 股东列表
        'maxholder': None,      # 最大股东
        'naturalMan': None,     # 自然人股东
        'enterprise': None      # 企业股东
    }

    # 找出关联表中该公司的股东id
    tempShareholderList = models.TMCorpCorpStock.objects.filter(id=cid, org=corg, seq_id=cseqId)

    # 找出股东表中这些股东的记录
    for e in tempShareholderList:
        stucture['shareholderList'].append(models.TCorpStock.objects.get(id=e.sub_id, org=e.sub_org, seq_id=e.sub_seq_id))

    # 查找最大股东
    maxcapi = 0
    for e in stucture['shareholderList']:
        if e.stock_capi > maxcapi:
            maxcapi = e.stock_capi
            stucture['maxholder'] = e

    # 查找自然人股东
    stucture['naturalMan'] = models.TCorpStock.objects.get(stock_type='自然人')

    # 查找企业股东
    stucture['enterprise'] = models.TCorpStock.objects.get(stock_type='企业')

    # 返回股权结构字典
    return stucture

# 企业图谱
def enterpriseAtlas(company):
    # 企业图谱字典
    atlas = {
        'shareholser': [],
        'seniorExecutive': [],
        'adjudicativeDoc': [],
        'courtAnnoun': [],
        'historicalShr': [],
        'histLegalPer': [],
        'outboundInvest': [],
    }

    # 股东
    ownership = ownershipStucture(company)
    atlas['shareholser'] = ownership['shareholderList']

    # 高管

    return atlas