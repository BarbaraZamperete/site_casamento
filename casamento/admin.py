from django.contrib import admin
from .models import Convidado, Presente, Compra, Loja

class ConvidadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'codigo_convite', 'na_lista', 'presenca_confirmada')
    search_fields = ('nome', 'email', 'codigo_convite')
    list_filter = ('na_lista', 'presenca_confirmada')

class PresenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'loja')
    search_fields = ('nome', 'descricao')
    list_filter = ('loja',)

class CompraAdmin(admin.ModelAdmin):
    list_display = ('convidado', 'presente', 'data_compra', 'valor_pago', 'status_pagamento')
    search_fields = ('convidado__nome', 'presente__nome')
    list_filter = ('status_pagamento',)

class LojaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'tipo')
    search_fields = ('nome', 'endereco')
    list_filter = ('tipo',)

# Register your models here.
admin.site.register(Convidado, ConvidadoAdmin)
admin.site.register(Presente, PresenteAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Loja, LojaAdmin)