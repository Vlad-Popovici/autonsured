from django.db import models
from django.utils.text import slugify
from django.forms import ModelForm
from . import choices

# Create your models here.
class Page(models.Model):
	title = models.CharField(max_length=80)
	slug = models.SlugField(unique=True)
	description = models.CharField(max_length=150)
	body = models.TextField(blank=True)

	def __str__(self):
		return self.title




class GetQuote(models.Model):
	
	#Step 1 - Personal Info:
	contact_first_name     = models.CharField(help_text="This is the help text!",max_length=100)
	contact_middle_name    = models.CharField(max_length=100)
	contact_last_name      = models.CharField(max_length=100)
	contact_street_address = models.CharField(max_length=250)
	contact_city           = models.CharField(max_length=100,choices=choices.CITY_CHOICES)
	contact_state          = models.CharField(max_length=100)
	contact_date_of_birth  = models.DateField(default='1900-10-10')

	#Step 2 - Vehicle:
	year           = models.CharField(default='1922',max_length=4,choices=choices.YEAR_CHOICES)
	make           = models.CharField(default='BMW',max_length=100,choices=choices.MAKE_CHOICES)
	car_model      = models.CharField(default='X3',max_length=100,choices=choices.MODEL_CHOICES)
	body_style     = models.CharField(default='style1',max_length=100,choices=choices.BODYSTYLE_CHOICES)
	vin            = models.CharField(default='IASJI21ej22',max_length=100) #vehicle identification number 
	
	#Step 3 - Drivers:
	#Are you the driver of this car  ? -Yes (if yes, auto-populate fields below with existing data) - No empty fields
	driver_confirmation    = models.CharField(default='Yes',max_length=3,choices=[('Yes','Yes'),('No','No')])
	driver1_first_name     = models.CharField(default='1922',help_text="This is the help text!",max_length=100)
	driver1_middle_name    = models.CharField(default='1922',max_length=100)
	driver1_last_name      = models.CharField(default='1922',max_length=100)
	driver1_street_address = models.CharField(default='1922',max_length=250)
	driver1_city           = models.CharField(default='New York',max_length=100,choices=choices.CITY_CHOICES)
	driver1_state          = models.CharField(default='1922',max_length=100)
	driver1_date_of_birth  = models.DateField(default='1901-10-10')

	#Option to add additional drivers
	driver2_first_name     = models.CharField(default='1922',blank=True,help_text="This is the help text!",max_length=100)
	driver2_middle_name    = models.CharField(default='1922',blank=True,max_length=100)
	driver2_last_name      = models.CharField(default='1922',blank=True,max_length=100)
	driver2_street_address = models.CharField(default='1922',blank=True,max_length=250)
	driver2_city           = models.CharField(default='LA',blank=True,max_length=100,choices=choices.CITY_CHOICES)
	driver2_state          = models.CharField(default='1922',blank=True,max_length=100)
	driver2_date_of_birth  = models.DateField(default='1902-10-10',blank=True)
	

	# #Step 4 - Driving History:

	# #Step 5 - Additional info:
	
	
	def __str__(self):
		return self.last_name

class GetQuoteForm(ModelForm):
	class Meta:
		model  = GetQuote
		fields = [
		#Step 1:
		'contact_first_name', 'contact_middle_name', 'contact_last_name', 'contact_street_address', 'contact_city', 
		'contact_state', 
		#Step 2:
		'year','make','car_model','body_style','vin','driver_confirmation',

		#Step 3 - Additional drivers:
		'driver1_first_name','driver1_middle_name','driver1_last_name','driver1_street_address','driver1_city',
		'driver1_state','driver1_date_of_birth',

		'driver2_first_name','driver2_middle_name','driver2_last_name','driver2_street_address','driver2_city',
		'driver2_state','driver2_date_of_birth',
		]