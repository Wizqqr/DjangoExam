from django.contrib import admin
from .models import Devis, YoutubeVideo, Gadget, ReviewGadget, Tag

admin.site.register(Devis)
admin.site.register(YoutubeVideo)
admin.site.register(Gadget)
admin.site.register(ReviewGadget)
admin.site.register(Tag)