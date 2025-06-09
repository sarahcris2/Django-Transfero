from django.shortcuts import render
from rest_framework import viewsets
from blog.serializers import TopicoSerializer
from blog.models import Topico

# Create your views here.
def blog(request):
    contexto ={
        'titulo' : 'jornada Viagem | Blog'
    }
    return render(request,
        'blog/index.html',
        contexto,
    )


class TopicoViewSet(viewsets.ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer


def artigos(request):
    #exibir todos os artigos
    exibe_artigos =  {
        'titulo' : 'jornada Viagem | Blog',
        'artigos': Topico.objects.all()

    }
    #Retornar os dados para a pagina
    return render(
        request,
        'blog/tabela.html',
        exibe_artigos,
    )