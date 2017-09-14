from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
from company.models import Company


def index(request):
    companys = Company.objects.all()
    data = {'companys': companys}
    return render_to_response('index.html',data)

def add(request):
    if request.method == 'POST':
        req = json.loads(request.body)