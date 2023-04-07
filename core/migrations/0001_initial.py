# Generated by Django 4.1.7 on 2023-04-03 21:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=255, null=True)),
                ('header_en', models.CharField(blank=True, max_length=255, null=True)),
                ('header_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('body_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('body_ar', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('about_image', models.ImageField(blank=True, max_length=254, null=True, upload_to='photos/')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200)),
                ('client_name_en', models.CharField(max_length=200, null=True)),
                ('client_name_ar', models.CharField(max_length=200, null=True)),
                ('review_message', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('review_message_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('review_message_ar', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('img', models.ImageField(blank=True, max_length=254, null=True, upload_to='client/')),
            ],
        ),
        migrations.CreateModel(
            name='Client_intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=255, null=True)),
                ('header_en', models.CharField(blank=True, max_length=255, null=True)),
                ('header_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('body_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('body_ar', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=255, null=True)),
                ('header_en', models.CharField(blank=True, max_length=255, null=True)),
                ('header_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('body_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('body_ar', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(blank=True, max_length=255, null=True)),
                ('feature_name_en', models.CharField(blank=True, max_length=255, null=True)),
                ('feature_name_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('feature', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('feature_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('feature_ar', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('feature_icon', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feature_intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('title_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('intro', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('intro_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('intro_ar', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('feature_image', models.ImageField(blank=True, max_length=254, null=True, upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('img', models.ImageField(blank=True, max_length=254, null=True, upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery_intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=255, null=True)),
                ('header_en', models.CharField(blank=True, max_length=255, null=True)),
                ('header_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('body_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('body_ar', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('title_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='')),
                ('apple', models.ImageField(blank=True, null=True, upload_to='')),
                ('navlogo', models.ImageField(blank=True, null=True, upload_to='')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=255, null=True)),
                ('tiktok_url', models.CharField(blank=True, max_length=255, null=True)),
                ('slider_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('slider_text', models.CharField(blank=True, max_length=255, null=True)),
                ('slider_text_en', models.CharField(blank=True, max_length=255, null=True)),
                ('slider_text_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('slider_header', models.CharField(blank=True, max_length=255, null=True)),
                ('slider_header_en', models.CharField(blank=True, max_length=255, null=True)),
                ('slider_header_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('footer_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('footer_address1', models.CharField(blank=True, max_length=255, null=True)),
                ('footer_address1_en', models.CharField(blank=True, max_length=255, null=True)),
                ('footer_address1_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('footer_address2', models.CharField(blank=True, max_length=255, null=True)),
                ('footer_address2_en', models.CharField(blank=True, max_length=255, null=True)),
                ('footer_address2_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('footer_text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('googel_map_url', models.CharField(blank=True, max_length=255, null=True)),
                ('working_hours', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Whyus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_ar', models.CharField(max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('body_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('body_ar', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, max_length=254, null=True, upload_to='photos/')),
            ],
        ),
    ]
