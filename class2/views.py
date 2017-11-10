from django.http import *
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from company.models import *
import datetime,json,sqlite3
@csrf_exempt 


def index(request):
    companys = Company.objects.all()
    historys = History.objects.all()
    data = {'companys': companys}
    data2 = {'historys': historys}
    return render_to_response('index.html',data,data2)



def add(request):
    if request.method == 'POST':
        companyName = request.POST['companyName']
        ownerName = request.POST['ownerName']
        print ownerName
        date = request.POST['date'].replace(',','').split()
        dtstr = "-".join(date) 
        dtstr = datetime.datetime.strptime(dtstr, "%B-%d-%Y").date()
        print type(dtstr)
        obj = Company(name=companyName,create_time=dtstr,update_time='',ownername=ownerName)
        obj.save()
        return render_to_response('index.html')

def update(request):
    if request.method == 'POST':
        id = request.POST['id'] 
        # ownername = request.POST['ownerName']
        # coreversion = request.POST['coreversion']  
         

        company = Company.objects.get(id=id)
        company.ownername = request.POST.get('ownerName', '')
        company.coreversion = request.POST.get('coreversion', '')
        company.remarks =  request.POST.get('remarks', '')
        company.webversion = request.POST.get('webversion', '')
        company.save()

        companyname = request.POST.get('companyname', '')
        ownername = request.POST.get('ownerName', '')
        coreversion = request.POST.get('coreversion', '')
        remarks =  request.POST.get('remarks', '')
        webversion = request.POST.get('webversion', '')
        create_time =  request.POST.get('create', '')
        update_time = request.POST.get('update', '')
        obj = History(name=companyname,create_time=create_time,update_time=update_time,ownername=ownername,webversion=webversion,coreversion=coreversion)
        obj.save()
    return render_to_response('index.html')


def rm(request):
    if request.method == 'GET':
        id = request.GET['id']
        date = Company.objects.get(id=id)
        date.delete()
    return HttpResponseRedirect('/')

# def __default(obj): 
#     if isinstance(obj, datetime): 
#         return obj.strftime('%Y-%m-%dT%H:%M:%S') 
#     elif isinstance(obj, date): 
#         return obj.strftime('%Y-%m-%d') 
#     else: 
#         raise TypeError('%r is not JSON serializable' % obj) 

def edit(request):
    if request.method == 'GET':
        id = request.GET['id']
        companys = Company.objects.get(id=id)
        create_time = companys.create_time.strftime("%Y-%m-%d")
        update_time = companys.update_time.strftime("%Y-%m-%d")

        data={"a": companys.name, "b":create_time,"c":update_time,"d":companys.ownername,"e":companys.coreversion,"f":companys.webversion,"g":companys.remarks}
        print data
        return HttpResponse(json.dumps(data))

def history(request):
    if request.method == 'GET':
        id = request.GET['id']
        companys = Company.objects.get(id=id)
        name = companys.name
        historys = History.objects.filter(name=name)
        print type(historys)
        print historys
        return HttpResponse(json.dumps(data))
