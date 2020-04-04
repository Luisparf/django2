from django.contrib import admin
from .models import Produto

@admin.register(Produto) #decorator para registro de produtos na pagina admin
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco','estoque', 'slug', 'criado', 'modificado', 'ativo')

