"""welljia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from helpers.authuser.engin_view import AuthEngine
from hello.engine_menu import PcMenu

from django.views.generic import RedirectView 
from webpage.page_home import Home
from webpage.page_huxing import  Huxing
from webpage.views import ZhanShi, Xuanchuan, PeiTao, D3Wrap, D3WrapE, Manual, FullHome


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/([\w\.]+)/?$',AuthEngine.as_view(),name=AuthEngine.url_name),
    
    url(r'^d/',include('helpers.director.urls'),name='director'),
    url(r'^zhanshi/?$', ZhanShi.as_view()), 
    url(r'^peitao/?$', PeiTao.as_view()), 
    url(r'^xuanchuan/?$', Xuanchuan.as_view()), 
    url(r'^manual/?$', Manual.as_view()), 
    
    url(r'^3d_wrap/?$', D3Wrap.as_view()), 
    url(r'^3d_wrap_e/?$', D3WrapE.as_view()),
    
    url(r'^pc/([\w\.]+)/?$',PcMenu.as_view(),name=PcMenu.url_name),
    url(r'^pc/?$',RedirectView.as_view(url='/pc/admin_user')), 
    url(r'^huxing/?$', Huxing.as_view()), 
    url(r'^digital', Home.as_view()), 
    url(r'^$', FullHome.as_view()), 
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
