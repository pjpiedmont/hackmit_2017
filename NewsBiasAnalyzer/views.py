from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    indexFile = open("index.html")
    return HttpResponse(indexFile)

@csrf_exempt
def analyze(request):
    print("yo")
    response = request.POST.get("address")
    return HttpResponse(response)