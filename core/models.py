from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime


class Header(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    apple = models.ImageField(null=True, blank=True)
    navlogo = models.ImageField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    slider_img_1 = models.ImageField(null=True, blank=True)
    slider_img_2 = models.ImageField(null=True, blank=True)
    slider_img_3 = models.ImageField(null=True, blank=True)
    slider_text_1 = models.CharField(max_length=255, null=True, blank=True)
    slider_text_2 = models.CharField(max_length=255, null=True, blank=True)
    slider_text_3 = models.CharField(max_length=255, null=True, blank=True)
    slider_header_1 = models.CharField(max_length=255, null=True, blank=True)
    slider_header_2 = models.CharField(max_length=255, null=True, blank=True)
    slider_header_3 = models.CharField(max_length=255, null=True, blank=True)
    footer_address1 = models.CharField(max_length=255, null=True, blank=True)
    footer_address2 = models.CharField(max_length=255, null=True, blank=True)
    footer_img = models.ImageField(null=True, blank=True)
    footer_text = RichTextField(null=True, blank=True)
    googel_map_url = models.CharField(max_length=255, null=True, blank=True)
    hero_img = models.ImageField(null=True, blank=True)
    slug =  models.SlugField(unique=True, null=True, blank=True )
    working_hours = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title or ' '

    def get_absolute_url(self):
        return reverse("header_list")

    @property
    def hero_imgimageURL(self):
        try:
            url = self.hero_img.url
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
    def appleimageURL(self):
        try:
            url = self.apple.url
        except:
            url = ''
        return url

    @property
    def iconimageURL(self):
        try:
            url = self.icon.url
        except:
            url = ''
        return url

    @property
    def sliderimageURL(self):
        try:
            url = self.slider_img.url
        except:
            url = ''
        return url

    @property
    def footerimgimageURL(self):
        try:
            url = self.footer_img.url
        except:
            url = ''
        return url


class About(models.Model):
    header = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    slug =  models.SlugField(unique=True, null=True, blank=True )

    def __str__(self):
        return self.header or ' '

    

    @property
    def imgimageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url


class Whyus(models.Model):
    number = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    slug =  models.SlugField(unique=True, null=True, blank=True )
    text = RichTextField(null=True, blank=True)



class Service(models.Model):
    icon = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    intro = RichTextField(null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    service_image = models.ImageField(null=True, blank=True)
    slug =  models.SlugField(unique=True, null=True, blank=True )
    
    @property
    def service_imageimageURL(self):
        try:
            url = self.service_image.url
        except:
            url = ''
        return url


    def __str__(self):
        return self.title


class Team(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    about_team = RichTextField(null=True, blank=True)
    profile_img = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    slug =  models.SlugField(unique=True, null=True, blank=True )


    @property
    def profile_imgimageURL(self):
        try:
            url = self.profile_img.url
        except:
            url = ''
        return url


class Cts(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    call_icon = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    slug =  models.SlugField(unique=True, null=True, blank=True )



class Client(models.Model):
    client_name = models.CharField(max_length=200)
    review_message = RichTextField(null=True, blank=True)
    img = models.ImageField(upload_to='client/',
                            max_length=254, null=True, blank=True)
    slug =  models.SlugField(unique=True, null=True, blank=True )
    position = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.client_name or ''

    @property
    def imgimageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url


class Project(models.Model):
    Service_category= models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="service_category")
    project_name= models.CharField(max_length=200)
    project_details= RichTextField(null=True, blank=True)
    project_client= models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True )
    project_img_1 = models.ImageField(
        upload_to='project/', null=True, blank=True)
    project_img_2 = models.ImageField(
        upload_to='project/', null=True, blank=True)
    project_img_3 = models.ImageField(
        upload_to='project/', null=True, blank=True)


    @property
    def project_img_1imageURL(self):
        try:
            url = self.project_img_1.url
        except:
            url = ''
        return url

    @property
    def project_img_2imageURL(self):
        try:
            url = self.project_img_2.url
        except:
            url = ''
        return url

    @property
    def project_img_3imageURL(self):
        try:
            url = self.project_img_3.url
        except:
            url = ''
        return url


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name
