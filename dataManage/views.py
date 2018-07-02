from django.shortcuts import render
from django.http import Http404
from django.shortcuts import HttpResponse
from dataManage import models
import json

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

    try:
        # 得到查找的公司
        company = models.TCorp.objects.get(corp_name=com_name)

    except models.TCorp.DoesNotExist:
        error_msg = '您查找的公司不存在！'
        return render(request, 'fail.html', {'error_msg': error_msg})

    # 得到股权结构信息
    structuredic = ownershipStucture(company)

    ownerlist = structuredic['shareholderList']              # 股东列表
    maxholder = structuredic['maxholder'].stock_name         # 最大股东
    naturalMan = structuredic['naturalMan'].stock_name       # 自然人股东
    enterprise = structuredic['enterprise'].stock_name       # 企业股东

    # 得到投资族谱信息
    investG = investmentGenealogy(com_name)

    dist_coms = investG[0]                                   # 分公司
    stock_companys = investG[1]                              # 股东再投资

    # 得到企业图谱信息
    atlas = enterpriseAtlas(company)

    seniorExve = atlas['seniorExecutive']

    return render(request, "result.html", {'company': company, 'ownerlist': ownerlist,
                                           'maxholder': maxholder, 'naturalMan': naturalMan,
                                           'enterprise': enterprise, 'dist_coms': dist_coms,
                                           'stock_companys': stock_companys, 'seniorExve': seniorExve,
                                           })

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

# 投资族谱
def investmentGenealogy(com_name):
    # 获取市场主体的联合主键
    com_org = models.TCorp.objects.get(corp_name=com_name).org
    com_id = models.TCorp.objects.get(corp_name=com_name).id
    com_seq_id = models.TCorp.objects.get(corp_name=com_name).seq_id

    # 市场主体对外投资

    # 通过市场主题的联合主键，在M4中寻找对外投资公司的记录
    dist_com_lists = models.TMCorpCorpDist.objects.filter(org=com_org, id=com_id, seq_id=com_seq_id)

    # 在公司表中获取分公司的记录
    dist_coms = []
    for com in dist_com_lists:
        dist_coms.append(models.TCorpDist.objects.get(org=com.sub_org, id=com.sub_id, seq_id=com.sub_seq_id))

    # 股东再投资
    # 通过市场主题的联合主键，在M4中寻找股东的记录
    stock_lists = models.TMCorpCorpStock.objects.filter(org=com_org, id=com_id, seq_id=com_seq_id)

    # 在股东表中获取股东记录
    stocks = []
    again_invest = []  # 存储每一个股东再投资的所有公司的列表
    stock_companys = dict()
    for stock in stock_lists:
        # 获取股东的记录
        the_stock = models.TCorpStock.objects.get(org=stock.sub_org, id=stock.sub_id, seq_id=stock.sub_seq_id)
        stocks.append(the_stock.stock_name)
        # stock_companys.append(the_stock.stock_name)

        # 获取每一个股东再投资的公司的记录
        stock_coms = models.TMCorpCorpStock.objects.filter(sub_org=the_stock.org, sub_id=the_stock.id,
                                                           sub_seq_id=the_stock.seq_id)  # 一个股东对应的多个公司主键
        for stock_com in stock_coms:
            if models.TCorp.objects.get(id=stock_com.id, org=stock_com.org,
                                        seq_id=stock_com.seq_id).corp_name not in again_invest:
                again_invest.append(
                    models.TCorp.objects.get(id=stock_com.id, org=stock_com.org, seq_id=stock_com.seq_id).corp_name)

        stock_companys[the_stock.stock_name] = again_invest

    return dist_coms, stock_companys

# 企业图谱
def enterpriseAtlas(company):
    cid = company.id
    corg = company.org
    cseqId = company.seq_id

    # json数据格式
    atlasdata = {
        'name': company.corp_name,
        'children': [
            {
                'name': "对外投资",
                'children': [],
            },
            {
                'name': "股东",
                'children': [],
            },
            {
                'name': "高管",
                'children': [],
            },
            {
                'name': "裁判文书",
                'children': [],
            },
            {
                'name': "法院公告",
                'children': [],
            },
            {
                'name': "历史股东",
                'children': [],
            },
            {
                'name': "历史法人",
                'children': [],
            },
        ]
    }

    # 字典
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

    lastAtlas = []
    for e in atlas['shareholser']:
        # json中的结点格式
        childnode = {'name': ""}
        childnode['name'] = e.stock_name
        lastAtlas.append(childnode)

    for e in atlasdata['children']:
        if e['name'] == "股东":
            e['children'] =lastAtlas

    # 高管
    seniorElist = models.TMCorpCorpPertains.objects.filter(org=corg, id=cid, seq_id=cseqId)
    SE = []
    # 属于本公司的职员
    for e in seniorElist:
        sorg = e.sub_org
        sid = e.sub_id
        sseqId = e.sub_seq_id
        SE.append(models.TCorpPertains.objects.get(org=sorg, id=sid, seq_id=sseqId))

    # 判断是否为高管
    def isSE(e):
        return ((e.person_type == '总经理') or (e.person_type == '副总经理') or (e.person_type == '董事长')
                or (e.person_type == '总工程师') or (e.person_type == '总经济师') or (e.person_type == '财务总监')
                or (e.person_type == '营销总监') or (e.person_type == '行政总监') or (e.person_type =='人事总监')
                or (e.person_type =='监事会总监'))

    SSE = filter(isSE, SE)
    # 将高管数据转化为json模式，存入json文件
    lastAtlas = []
    for e in SSE:
        # json中的结点格式
        childnode = {'name': ""}
        childnode['name'] = e.person_name
        lastAtlas.append(childnode)
        atlas['seniorExecutive'].append(e.person_name)

    for e in atlasdata['children']:
        if e['name'] == "高管":
            e['children'] = lastAtlas

    fw = open('static/json/enterpriseAtlas.json', 'w', encoding='utf-8')  # 打开一个名字为‘enterpriseAtlas.json’的空文件
    atlasjson = json.dump(atlasdata, fw, ensure_ascii=False, indent=4)
    fw.close()

    return atlas