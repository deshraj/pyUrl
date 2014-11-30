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
from django.template imporpt Context
# from stickers.models import *
import random,string

def home(request):
	# request.session.set_test_cookie()
	# if request.session.test_cookie_worked():
	# 	print 'hello'
	#custId=''.join([random.choice(string.letters + string.digits) for i in range(10)])
	return render_to_response("index.html",context_instance=RequestContext(request))
