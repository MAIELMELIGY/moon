from django.contrib import admin

from.models import Header,Client_intro ,About,Client,Feature,Gallery,Gallery_intro,Contact_intro,Feature_intro,Whyus
from  django.contrib.auth.models  import  Group  # new
#...

admin.site.unregister(Group)  # new
admin.site.register(Header)
admin.site.register(About)
admin.site.register(Feature)
admin.site.register(Client)
admin.site.register(Gallery_intro)
admin.site.register(Gallery)
admin.site.register(Client_intro)
admin.site.register(Contact_intro)
admin.site.register(Whyus)
admin.site.register(Feature_intro)