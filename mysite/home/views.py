from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
	return render(request, 'home/index.html', content_type="text/html")
    # return HttpResponse("Hello, world. Your momma.")
