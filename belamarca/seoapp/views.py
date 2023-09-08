from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET


#--------------------------------------
# View usada para gerar o robots.txt
#--------------------------------------
@require_GET
def robots_txt(request):
    current_url = request.build_absolute_uri('/')[:-1]

    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: *utm*",
        "Sitemap: {url}/sitemap.xml".format(url=current_url),
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")