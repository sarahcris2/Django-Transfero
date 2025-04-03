from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog(request):
    #print('pasei pelo blog')
#HttpResponse('<body bgcolor="green"><h1>Ola mundo</h1></body>')
    return render(
        request,
        'blog/index.html'
    )

def artigo(request):
    return render(
        request,
        'blog/artigo.html'
    )
