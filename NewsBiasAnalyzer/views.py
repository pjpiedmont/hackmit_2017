from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import random

def index(request):
    indexFile = open("index.html")
    return HttpResponse(indexFile)

@csrf_exempt
def analyze(request):
    print("yo")
    response = random.randrange(0, 101)
    return HttpResponse(response)