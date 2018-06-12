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

    #第二题

    #获取市场主体的联合主键
    com_org = models.TCorp.objects.get(corp_name=com_name).org
    com_id = models.TCorp.objects.get(corp_name=com_name).id
    com_seq_id = models.TCorp.objects.get(corp_name=com_name).seq_id

    # 市场主体对外投资

    #通过市场主题的联合主键，在M4中寻找对外投资公司的记录
    dist_com_lists = models.TMCorpCorpDist.objects.filter(org=com_org, id=com_id, seq_id=com_seq_id)

    #在公司表中获取分公司的记录
    dist_coms =[]
    for com in dist_com_lists:
        dist_coms.append(models.TCorpDist.objects.get(org=com.sub_org, id=com.sub_id, seq_id=com.sub_seq_id))

    # 股东再投资
     # 通过市场主题的联合主键，在M4中寻找股东的记录
    stock_lists = models.TMCorpCorpStock.objects.filter(org=com_org, id=com_id, seq_id=com_seq_id)

    # 在股东表中获取股东记录
    stocks = []
    again_invest=[]   #存储每一个股东再投资的所有公司的列表
    stock_companys=dict()
    for stock in stock_lists:
        # 获取股东的记录
        the_stock=models.TCorpStock.objects.get(org=stock.sub_org, id=stock.sub_id, seq_id=stock.sub_seq_id)
        stocks.append(the_stock.stock_name)
        #stock_companys.append(the_stock.stock_name)

        #获取每一个股东再投资的公司的记录
        stock_coms=models.TMCorpCorpStock.objects.filter(sub_org=the_stock.org, sub_id=the_stock.id, sub_seq_id=the_stock.seq_id)  #一个股东对应的多个公司主键
        for stock_com in stock_coms:
            if models.TCorp.objects.get(id=stock_com.id, org=stock_com.org, seq_id=stock_com.seq_id).corp_name not in again_invest:
                again_invest.append(models.TCorp.objects.get(id=stock_com.id, org=stock_com.org, seq_id=stock_com.seq_id).corp_name)

        stock_companys[the_stock.stock_name]=again_invest




    return render(request, "result.html", {'company': company, 'ownerlist': ownerlist,
                                           'maxholder': maxholder, 'naturalMan': naturalMan,
                                           'enterprise': enterprise, 'dist_coms': dist_coms,
                                           'stock_companys': stock_companys})

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
