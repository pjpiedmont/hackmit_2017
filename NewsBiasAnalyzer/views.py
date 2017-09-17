from django.http import HttpResponse

def index(request):
    indexFile = open("index.html")
    return HttpResponse(indexFile)

def analyze(request):
    return HttpResponse("hey")