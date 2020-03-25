from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages  # import para messages.sucess


def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)  # variavel form pode ser formulario preenchido com dados do metodo POST ou vazia

    if str(request.method) == 'POST':  # se o usuario tenta submeter dados com metodo POST
        if form.is_valid():  # se o formulario é valido (metodo is_valid da classe Form retorna True se formulario nao possui erros
            nome = form.cleaned_data['nome']  # pega dados
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada')
            print(f"Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}")

            messages.success(request, 'E-mail enviado com sucesso')  # mensagem no contexto da pagina (caso de sucesso)

            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')  # mensagem no contexto da pagina (caso de erro)

    context = {
        'form': form
    }
    return render(request, 'contato.html', context) #envia o contexto para o template


def produto(request):
    return render(request, 'produto.html')
