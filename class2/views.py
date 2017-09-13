from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')
    
def add(request):
     if request.method == 'POST':
        received_json_data = json.loads(request.body)
        print (received_json_data1)