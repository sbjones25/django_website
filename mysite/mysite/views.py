from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. default view motha fucka")

def index(request):
	return render(request, 'index.html', content_type="text/html")
