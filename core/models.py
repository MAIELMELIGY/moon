from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db import models
from django.urls import reverse
class Header(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	icon = models.ImageField(null=True, blank=True)
	apple = models.ImageField(null=True, blank=True)
	navlogo = models.ImageField(null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	facebook_url = models.CharField(max_length=255, null=True, blank=True)
	instagram_url = models.CharField(max_length=255, null=True, blank=True)
	linkedin_url = models.CharField(max_length=255, null=True, blank=True)
	twitter_url = models.CharField(max_length=255, null=True, blank=True)
	tiktok_url = models.CharField(max_length=255, null=True, blank=True)
	slider_img = models.ImageField(null=True, blank=True)
	slider_text = models.CharField(max_length=255, null=True, blank=True)
	slider_header = models.CharField(max_length=255, null=True, blank=True)
	footer_img = models.ImageField(null=True, blank=True)
	footer_address1 = models.CharField(max_length=255, null=True, blank=True)
	footer_address2 = models.CharField(max_length=255, null=True, blank=True)
	footer_text = RichTextField(null=True, blank=True)
	googel_map_url = models.CharField(max_length=255, null=True, blank=True)
	working_hours = models.CharField(max_length=255, null=True, blank=True)
	def __str__(self):
		return self.title or ''


	@property
	def iconURL(self):
		try:
			url = self.icon.url
		except:
			url = ''
		return url

	@property
	def appleimageURL(self):
		try:
			url = self.apple.url
		except:
			url = ''
		return url

	@property
	def navlogoimageURL(self):
		try:
			url = self.navlogo.url
		except:
			url = ''
		return url

	@property
	def slider_imgimageURL(self):
		try:
			url = self.slider_img.url
		except:
			url = ''
		return url
	@property
	def footer_imgimageURL(self):
		try:
			url = self.footer_img.url
		except:
			url = ''
		return url
class Feature_intro(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)
	intro = RichTextField(null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	feature_image = models.ImageField(upload_to='photos/', max_length=254,null=True, blank=True)
	def __str__(self):
		return self.title or ''	
	@property
	def feature_imageimageURL(self):
		try:
			url = self.feature_image.url
		except:
			url = ''
		return url

	
class Feature(models.Model):
	feature_name = models.CharField(max_length=255, null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	feature = RichTextField(null=True, blank=True)
	feature_icon = models.CharField(max_length=255, null=True, blank=True)
	def __str__(self):
		return self.feature_name or ''


class Whyus(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	body = RichTextField(null=True, blank=True)
	img = models.ImageField(upload_to='photos/', max_length=254,null=True, blank=True)
	def __str__(self):
		return self.title or ''

	@property
	def imgimageURL(self):
		try:
			url = self.img.url
		except:
			url = ''
		return url

	
class About(models.Model):
	header = models.CharField(max_length=255, null=True, blank=True)
	body = RichTextField(null=True, blank=True)
	about_image = models.ImageField(upload_to='photos/', max_length=254,null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	def __str__(self):
		return self.header or ''

	@property
	def about_imageimageURL(self):
		try:
			url = self.about_image.url
		except:
			url = ''
		return url

class Gallery_intro(models.Model):
	header = models.CharField(max_length=255, null=True, blank=True)
	body = RichTextField(null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	def __str__(self):
		return self.header or ''

class Gallery(models.Model):
	slug = models.SlugField(max_length=250,null = True, blank = True)
	img = models.ImageField(upload_to='photos/', max_length=254,null=True, blank=True)
	@property
	def imgimageURL(self):
		try:
			url = self.img.url
		except:
			url = ''
		return url

class Client_intro(models.Model):
	header = models.CharField(max_length=255, null=True, blank=True)
	body = RichTextField(null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	def __str__(self):
		return self.header or ''



class Contact_intro(models.Model):
	header = models.CharField(max_length=255, null=True, blank=True)
	body = RichTextField(null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	def __str__(self):
		return self.header or ''

class Client(models.Model):
	client_name = models.CharField(max_length=200)
	review_message = RichTextField(null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	img = models.ImageField(upload_to='client/', max_length=254,null=True, blank=True)
	def __str__(self):  
		return self.client_name or ''  
	@property
	def imgimageURL(self):
		try:
			url = self.img.url
		except:
			url = ''
		return url   