from django.http import *
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from company.models import *
import datetime,json 
@csrf_exempt 


def index(request):
    companys = Company.objects.all()
    data = {'companys': companys}
    return render_to_response('index.html',data)


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
        print id
        company = Company.objects.get(id = id)  
        company.ownername = request.POST['ownerName']  
        company.coreversion = request.POST['coreversion']  
        company.remarks =  request.POST['remarks']  
        company.webversion = request.POST['webversion'] 
        print company.ownername,company.coreversion,company.remarks,company.webversion
        company.save()
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
        data={"a": companys.name, "b":create_time,"c":update_time,"d":companys.ownername}
        print data
        return HttpResponse(json.dumps(data))