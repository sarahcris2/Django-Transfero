from django.http import HttpResponse
import socket
def home( request):
   # hostname = socket.gethostname()
  #  message = f"Ola visitante de {hostname} - create by Sarah"
    message = ("<body bgcolor='gold'<h1>Sarah Cristina</h1></body>")
    return HttpResponse(message)
