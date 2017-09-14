from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from company.models import *
@csrf_exempt 


def index(request):
    companys = Company.objects.all()
    data = {'companys': companys}
    return render_to_response('index.html',data)

def add(request):
    if request.method == 'POST':
        companyName = request.POST['companyName']
        date = request.POST['date']
        print companyName,date
        obj = Company(name=companyName,create_time=date,update_time='')
        obj.save()
        return render_to_response('index.html')
