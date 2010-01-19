# Create your views here.
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from presentations.slideshare.models import Slideshare

def about(request):
    """docstring for about"""
    return HttpResponse("This is the about page")
    
def demo(request):
    """docstring for about"""
    return render_to_response('slideshare/demo.html')
    
def show(request, object_id):
    """Show a presentation"""
    #return HttpResponse("Show a presentation: " + object_id)
    pres = Slideshare.objects.get(id=int(object_id))
    return render_to_response('slideshare/presentation.html', {'pres':pres})
    