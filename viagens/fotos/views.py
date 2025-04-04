from django.shortcuts import render

# Create your views here.
def fotos(request):
    contexto = {
        'titulo' : 'jornada Viagem | Fotos'
    }
    return render(
        request,
        'fotos/index.html',
        contexto,
    )