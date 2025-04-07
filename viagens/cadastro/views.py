from django.shortcuts import render

from cadastro.models import Pessoa

# Create your views here.
def cadastro(request):
    contexto ={
        'titulo' : 'jornada Viagem | Cadastro',
        'pessoas': Pessoa.objects.all(),
    }
    return render(request,
                      'cadastro/index.html',
                      contexto
                      )

def gravar(request):
    # salvar os dados da tela no banco
    nova_pessoa = Pessoa()
    nova_pessoa.nome     = request.POST.get("nome")
    nova_pessoa.telefone = request.POST.get("movel")
    nova_pessoa.email    = request.POST.get("correio")
    nova_pessoa.save()

    return cadastro(request)