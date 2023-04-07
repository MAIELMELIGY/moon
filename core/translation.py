from modeltranslation.translator import translator, TranslationOptions
from .models import Header , Client_intro,About,Gallery_intro , Whyus ,Feature ,Feature_intro,Client,Contact_intro

class HeaderTranslationOptions(TranslationOptions):
    fields = ('title', 'slider_text','slider_header','footer_address1','footer_address2')

translator.register(Header, HeaderTranslationOptions)

class AboutTranslationOptions(TranslationOptions):
    fields = ('header', 'body',)

translator.register(About, AboutTranslationOptions)
class Gallery_introTranslationOptions(TranslationOptions):
    fields = ('header', 'body',)

translator.register(Gallery_intro, Gallery_introTranslationOptions)
class Client_introTranslationOptions(TranslationOptions):
    fields = ('header', 'body',)

translator.register(Client_intro, Client_introTranslationOptions)

class WhyusTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)

translator.register(Whyus, WhyusTranslationOptions)

class FeatureTranslationOptions(TranslationOptions):
    fields = ('feature_name','feature',)

translator.register(Feature, FeatureTranslationOptions)

class Feature_introTranslationOptions(TranslationOptions):
    fields = ('title','intro',)

translator.register(Feature_intro, Feature_introTranslationOptions)

class ClientTranslationOptions(TranslationOptions):
    fields = ('client_name','review_message',)

translator.register(Client, ClientTranslationOptions)
class Contact_introTranslationOptions(TranslationOptions):
    fields = ('header', 'body',)

translator.register(Contact_intro, Contact_introTranslationOptions)