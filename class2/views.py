from django.http import *
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from company.models import *
import datetime
@csrf_exempt 


def index(request):
    companys = Company.objects.all()
    data = {'companys': companys}
    return render_to_response('index.html',data)

def add(request):
    if request.method == 'POST':
        companyName = request.POST['companyName']
        date = request.POST['date'].replace(',','').split()
        dtstr = "-".join(date) 
        dtstr = datetime.datetime.strptime(dtstr, "%B-%d-%Y").date()
        print type(dtstr)
        obj = Company(name=companyName,create_time=dtstr,update_time='')
        obj.save()
        return render_to_response('index.html')


def rm(request):
    if request.method == 'GET':
        id = request.GET['id']
        date = Company.objects.get(id=id) 
        date.delete()
    return HttpResponseRedirect('/')