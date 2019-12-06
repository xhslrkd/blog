from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from base.forms import ContactForm
from base.forms import SubscriberForm  
def index(request):
	return render(request, 'index.html', {'title':'Home'})
	
def resume(request):
	return render(request, 'resume.html', {'title':'Bio/Resume'})

def portfolio(request):
	return render(request, 'portfolio.html', {'title':'Projects'})


def gallery(request):
	return render(request, 'gallery.html', {'title':'Gallery'})


def log_in(request):
	form = SubscriberForm()
	return render(request, 'log_in.html', {'form': form, 'title': 'Subscriber Sign in/up'})

def email(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['Subject']
			message = form.cleaned_data['Message']
			email = form.cleaned_data['Email']
			cc_myself = form.cleaned_data['CC_myself']
			recipients = ['dongkang359@gmail.com']
			if cc_myself:
				recipients.append(email)
				send_mail(subject, message, email, recipients, fail_silently=False,)
			return HttpResponseRedirect('/resume/')
	else:
		form = ContactForm()
		return render(request, 'email.html', {'form': form, 'title':'Contact'})
