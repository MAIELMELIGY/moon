from modeltranslation.translator import translator, TranslationOptions
from .models import Header , About , Whyus ,Service , Cts , Team ,Client , Project

class HeaderTranslationOptions(TranslationOptions):
    fields = ('title', 'slider_text_1','slider_text_2','slider_text_3','slider_header_1','slider_header_2','slider_header_3','footer_address1','footer_address2',)

translator.register(Header, HeaderTranslationOptions)

class AboutTranslationOptions(TranslationOptions):
    fields = ('header', 'body',)

translator.register(About, AboutTranslationOptions)

class WhyusTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

translator.register(Whyus, WhyusTranslationOptions)

class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'intro','text',)

translator.register(Service, ServiceTranslationOptions)

class CtsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

translator.register(Cts, CtsTranslationOptions)
class TeamTranslationOptions(TranslationOptions):
    fields = ('title', 'about_team','name','position',)

translator.register(Team, TeamTranslationOptions)



class ClientTranslationOptions(TranslationOptions):
    fields = ('client_name','review_message',)

translator.register(Client, ClientTranslationOptions)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('project_name','project_details',)

translator.register(Project, ProjectTranslationOptions)