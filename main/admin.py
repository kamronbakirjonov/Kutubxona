from django.contrib import admin

from .models import *

admin.site.register(
    [Talaba, Mualif, Kitob, Kutubxonachi, Record]
)