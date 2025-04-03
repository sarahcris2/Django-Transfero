from django.shortcuts import render

# Create your views here.
def pacotes(request):
    return render(
        request,
        'pacotes/index.html'
    )
