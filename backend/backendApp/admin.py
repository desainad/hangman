from django.contrib import admin

# Register your models here.
from backendApp.models import *

admin.site.register(s_country)
admin.site.register(s_genre)
admin.site.register(s_artist)
admin.site.register(s_movie)
admin.site.register(s_profession)
admin.site.register(s_track)
admin.site.register(s_language)
admin.site.register(s_mv_artst_prfssn)
admin.site.register(s_mv_cmpny)
admin.site.register(s_company)

