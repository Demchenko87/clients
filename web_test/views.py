from django.http import HttpResponse

def clients(request):
    return HttpResponse('<h1>Hi Roman</h1>')