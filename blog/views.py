from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import datetime

# Create your views here.
def home(request):
	time = datetime.datetime.now()	
	return render_to_response('index.html',locals(),context_instance=RequestContext(request))

def about(request):
	return render_to_response('about.html',locals(),context_instance=RequestContext(request))



