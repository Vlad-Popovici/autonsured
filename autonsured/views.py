from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .models import Page, GetQuoteForm, GetQuote
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def home(request):
	return render(request, 'autonsured/base.html', {'home':home})

slug_list = []
for i in Page.objects.all():
	slug_list.append(i.slug)

def other_page(request,randomurl):
	#check if randomurl exists/matches slugs in Page.objects.all().slug
	if randomurl in slug_list:
		return render(request, 'autonsured/base.html')
	else:
		return HttpResponseNotFound()

def thank_you(request):
	return render(request, 'autonsured/thanks.html', {'thank_you':thank_you})

def contact_form_view(request):
	# if this is a POST request we need to process the form data
	if  request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			name    = form.cleaned_data['name']
			email   = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']

			recipients = ['mrvladpopovici@gmail.com']
			#send_mail(subject, message, email, recipients)
			
			# redirect to a new URL:
			return HttpResponseRedirect('/thank-you')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = ContactForm()
		return render(request, 'autonsured/form.html', {'form':form})


def get_quote(request):
	if request.method == 'POST':
		gform = GetQuoteForm(request.POST)
		if gform.is_valid():
			gform.save()

		return HttpResponseRedirect('/thank-you')

	else:
		gform = GetQuoteForm().as_ul()
		return render(request, 'autonsured/quoteform.html', {'gform':gform})

