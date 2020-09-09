from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import SateliteTelemetry, AntenaPositions, AntenaMoviment, SateliteMensagem

admin.site.register(SateliteTelemetry)
admin.site.register(AntenaPositions)
admin.site.register(AntenaMoviment)
admin.site.register(SateliteMensagem)