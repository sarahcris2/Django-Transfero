from django.shortcuts import render

# Create your views here.
def blog(request):
    contexto ={
        'titulo' : 'jornada Viagem | Blog'
    }
    return render(request,
        'blog/index.html',
        contexto,
    )

