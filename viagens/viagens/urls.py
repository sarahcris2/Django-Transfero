# """
# URL configuration for viagens project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from django.contrib.auth.views import LoginView


from django.conf import settings
from rest_framework import routers
from blog.views import TopicoViewSet


router = routers.DefaultRouter()
router.register('blog',TopicoViewSet)


urlpatterns = [
    path('',include('home.urls')),
    path('home/',include('home.urls')),
    path('blog/',include('blog.urls')),
    path('pacotes/',include('pacotes.urls')),
    path('fotos/',include('fotos.urls')),
    path('cadastro/',include('cadastro.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns +=[
    path('accounts/', include('django.contrib.auth.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)