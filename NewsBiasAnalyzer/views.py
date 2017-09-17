from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import NewsBiasAnalyzer.vectorize as vectorize

def index(request):
    indexFile = open("index.html")
    return HttpResponse(indexFile)

@csrf_exempt
def analyze(request):
    v = vectorize.vectorize()
    response = v.getValue(request.POST.get('text'))
    return HttpResponse(response)