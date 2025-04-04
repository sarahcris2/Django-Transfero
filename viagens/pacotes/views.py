from django.shortcuts import render

# Create your views here.
def pacotes(request):
    contexto = {
        'titulo' : 'Jornada Viagem | Pacotes'
    }
    return render(
        request,
        'pacotes/index.html',
        contexto,
    )
