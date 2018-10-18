from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('getquote', views.get_quote),
	path('contact', views.contact_form_view, name='form'),
	path('thank-you', views.thank_you, name='thank_you'),
	path('<randomurl>', views.other_page), #how do i limit this so if the article doesnt exist it shows a 404
]