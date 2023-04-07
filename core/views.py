from django.shortcuts import render, redirect
from .models import *
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.utils.translation import activate, get_language_info
from django.utils import translation
import django.utils.translation
from project import settings
# from django.utils.translation import LANGUAGE_SESSION_KEY
from django.db.models import Count
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage


def home(request):
	headers = Header.objects.all()
	abouts = About.objects.all()
	whyus = Whyus.objects.all()
	clients = Client.objects.all()
	features = Feature.objects.all()
	gallery = Gallery.objects.all()
	feature_intro = Feature_intro.objects.all()
	gallery_intro = Gallery_intro.objects.all()
	client_intro = Client_intro.objects.all()
	contact_intro = Contact_intro.objects.all()
	context = {
			'whyus': whyus, 
			'features': features, 
			'headers': headers,
			'abouts': abouts,
			'clients': clients, 
			'gallery': gallery, 
			'feature_intro':feature_intro,
			'gallery_intro':gallery_intro,
			'client_intro':client_intro,
			'contact_intro':contact_intro
		
			}
	return render(request, 'core/home.html', context)



def change_language(request):
	current_language = translation.get_language() 
	if current_language == "ar":
		lang_code ="en"
	else:
		lang_code = "ar"
	response = HttpResponseRedirect(request.POST.get('return_url',''))
	response.set_cookie(settings.LANGUAGE_COOKIE_NAME,lang_code)
	translation.activate(lang_code)
	return response