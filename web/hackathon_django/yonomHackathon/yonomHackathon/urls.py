"""yonomHackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from yonomApp import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.test2, name="test2"),
    path('web_home', views.web_home, name="web_home"),
    path('game_home/', views.game_home, name="game_home"),
    path('game_login/', views.game_login, name="game_login"),
    path('game_result', views.game_result, name="game_result"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)