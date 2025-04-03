from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
   # lista = '<ol><li>Sarah</li><li><Vanessa</li></ol>'
    #return HttpResponse(lista)
      return render(
        request,
        'home/index.html'
    )
