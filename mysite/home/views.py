from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse

import json, pprint
import flickr.flickr as flickr


flickr.API_KEY ='de251aa17812114888a4378204312a82'
flickr.API_SECRET = '8d45e742fabae9a8'

def index(request):
    return render(request, 'home/index.html', content_type="text/html")
    # return HttpResponse("Hello, world. Your momma.")

def search(request):
    query =  request.GET.get('search',None)
    photos = flickr.photos_search(text=str(query),sort='relevance')
    
    response = []
    for p in photos:
        image = {}
        image['img'] = p.getLarge()
        image['thumb'] = p.getThumbnail()
        response.append(image)
        print p.getLarge()

    return JsonResponse(response,safe=False)

