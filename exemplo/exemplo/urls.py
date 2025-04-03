# """
# URL configuration for exemplo project.

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
#funçoes para carregar views diretamente
# from blog import views as views_blog
# from home import views as views_home
from contato import views as views_contato

urlpatterns = [
    path('',include('home.urls')),
    path('home/',include('home.urls')),
    path('blog/', include('blog.urls')),
    # path('blog/',views_blog.blog ),
    path('contato/',views_contato.contato),
    path('admin/', admin.site.urls),
]
