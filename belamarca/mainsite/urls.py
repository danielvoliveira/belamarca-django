"""mainsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

# Importações relacionadas a SEO
from cms.sitemaps import CMSSitemap
from django.contrib.sitemaps.views import sitemap
from seoapp.views import robots_txt
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("sitemap.xml", cache_page(60 * 15)(sitemap), {"sitemaps": {
         "cmspages": CMSSitemap}}),
    path("robots.txt", cache_page(60 * 15)(robots_txt)),
]

urlpatterns += [
    re_path(r'^admin/', admin.site.urls),
    path("informacoes/", include("genericapp.urls")),
    path("formapp/", include("formapp.urls")),
    path("produto/", include("productapp.urls")),
    re_path(r'^', include('cms.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
