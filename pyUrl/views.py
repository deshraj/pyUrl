from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import *
from django.conf import settings
# import mongoengine
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import random,string
from pyUrl.models import * 

def home(request):
	random1 = None
	a = None
	if request.POST:
		url = request.POST['url']
		costumurl = request.POST['costumurl']
		# print costumurl
		a= urldata1.objects.filter(shortUrl__icontains = costumurl)
		if a:
			msg= "This url has already been taken."
			return render_to_response("index.html",{'a':a},
                           context_instance=RequestContext(request))
		else:
			if not costumurl:
				random1=''.join([random.choice(string.letters + string.digits) for i in range(5)])
				shortUrl = str(random1)
				# print shortUrl
			else:
				shortUrl = costumurl
			urldata1(url = url,shortUrl = shortUrl).save()
		return render_to_response("shorten.html",{"shortUrl" : "http://pyUrl.com/"+str(shortUrl),'a':a},
                           context_instance=RequestContext(request))
		# return render_to_response("index.html",{'shortUrl':1},c)
	# request.session.set_test_cookie()
	# if request.session.test_cookie_worked():
	# 	print 'hello'
	#geo=''.join([random.choice(string.letters + string.digits) for i in range(10)])
	return render_to_response("index.html",context_instance=RequestContext(request))

# def shorten(request):
# 	if request.POST:
# 		url = request.POST['url']
# 		random=''.join([random.choice(string.letters + string.digits) for i in range(10)])
# 		shortUrl = "http://pyUrl.com/"+str(random)
# 		print shortUrl
# 		return render_to_response("index.html",{'shortUrl':shortUrl},context_instance=RequestContext(request))
# 	return render_to_response("shorten.html")
def open(request,url=None):
	print "url sdfsafgasdeqatta"
	if request.path=='/':
		return render_to_response("index.html",context_instance=RequestContext(request))
	# print "check below one "
	# print request.path
	# print "just above one "
	try:
		out = urldata1.objects.get(shortUrl=str(request.path)[1:])
		urlOut = str(out.url)
		return HttpResponseRedirect(urlOut)
	except:
		return HttpResponse('<h2>The given url link is invalid. Please try another.</h2>')
