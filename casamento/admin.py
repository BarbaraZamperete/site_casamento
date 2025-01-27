from django.contrib import admin
from .models import Convidado, Presente, Compra

# Register your models here.
admin.site.register(Convidado)
admin.site.register(Presente)
admin.site.register(Compra)