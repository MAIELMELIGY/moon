from django.shortcuts import render, redirect
from .models import *
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import activate, get_language_info
from django.utils import translation
import django.utils.translation
from project import settings
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.db.models import Count
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from .forms import ContactForm

def home(request):
	headers = Header.objects.all()
	abouts = About.objects.all()
	whyuss = Whyus.objects.all()
	services = Service.objects.all()
	ctss = Cts.objects.all()
	teams = Team.objects.all()
	Clients = Client.objects.all()
	projects = Project.objects.annotate(
		Count('project_name_en')).order_by('-project_name_en__count')[:5]
	context = {'teams': teams, 'ctss': ctss, 'headers': headers, 'abouts': abouts,
			   'whyuss': whyuss, 'services': services, 'Clients': Clients, 'projects': projects}
	return render(request, 'core/index.html', context)


def service(request ,slug):
	headers = Header.objects.all()
	services= get_object_or_404(Service,slug=slug)
	context = {'services': services,'headers':headers}

	return render(request,'core/service_detail.html',context)




def project(request,slug):
	headers = Header.objects.all()
	projects= get_object_or_404(Project,slug=slug)
	context = {'projects': projects,'headers':headers}

	return render(request,'core/project_detail.html',context)


def change_language(request):
	current_language = translation.get_language()
	if current_language == "ar":
		lang_code = "en"
	else:
		lang_code = "ar"
	response = HttpResponseRedirect(request.POST.get('return_url', ''))
	response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
	translation.activate(lang_code)
	return response



def contact(request):
	headers = Header.objects.all()
	if request.method == 'POST':
		subject = request.POST.get('subject')
		Message = request.POST.get('message')
		email = request.POST.get('email')
		name = request.POST.get('name')
		message = f"name:{name}\nemail:{email}\nmessage:{Message}"
		send_mail(subject,message, email,
		[settings.EMAIL_HOST_USER,'mairshad238@gmail.com'], fail_silently=False)
		return render(request, 'core/index.html', {'email': email,'headers':headers,})

	return render(request, 'core/index.html', {'headers':headers,})