from django.shortcuts import render, redirect
from django.contrib import messages  # import para messages.sucess
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)  # variavel form pode ser formulario preenchido com dados do metodo POST ou vazia

    if str(request.method) == 'POST':  # se o usuario tenta submeter dados com metodo POST (str converte para string)
        if form.is_valid():  # se o formulario é valido (metodo is_valid da classe Form retorna True se formulario nao possui erros
            form.send_email()
            messages.success(request, 'E-mail enviado com sucesso')  # mensagem no contexto da pagina (caso de sucesso)
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')  # mensagem no contexto da pagina (caso de erro)

    context = {
        'form': form
    }
    return render(request, 'contato.html', context) #envia o contexto para o template


def produto(request):

    if str(request.user) != 'AnonymousUser': #se usuario esta logado e validado...
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)  # POST para dados e FILE para as imagens (upload)
            if form.is_valid(): #verifica se todos os campos foram preenchidos corretamente
                form.save() #se form é valido, salva
                messages.success(request, 'Produto salvo com sucesso')
                form = ProdutoModelForm()
            else:
                messages.success(request, 'Erro, verifique o formulario')
        else:
            form = ProdutoModelForm() #se request nao for do tipo POST apenas instancia um form,
        context = {
            'form': form #coloca num contexto,
        }
        return render(request, 'produto.html', context) #e renderiza
    else:
        return redirect('index') #se nao esta logado redireciona para index
