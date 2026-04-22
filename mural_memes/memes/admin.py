from django.contrib import admin
from .models import Meme


@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'categoria', 'criado_em')
    list_filter   = ('categoria',)
    search_fields = ('titulo', 'descricao')
    readonly_fields = ('criado_em',)
