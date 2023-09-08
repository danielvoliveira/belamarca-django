from django import template
from django.template.loader import get_template
from seoapp.models import SeoMetaTags
from cms.models.pagemodel import Page

def change_http_to_https(url):
    if 'http://' in url:
        url = url.replace('http://', 'https://')

    return url

register = template.Library()

@register.filter
def seo_tags(request):
    path = request.path
    current_url = change_http_to_https(request.build_absolute_uri(path))
    current_domain = change_http_to_https(request.build_absolute_uri('/')[:-1])

    path_first_position = path.split('/')[1]

    must_create_seo = False
    if path_first_position != 'admin':
        cms_pages = Page.objects.filter()
        for page in cms_pages:
            if page.is_home == True:
                must_create_seo = True

    if must_create_seo == True:
        current_meta_tags = SeoMetaTags.objects.filter(path=path)
        if len(current_meta_tags) == 0:
            current_meta_tags = SeoMetaTags(path=path)
            current_meta_tags.save()

        current_meta_tags = SeoMetaTags.objects.filter(path=path).values()

        social_media_image_url = ''
        if '/static/' in current_meta_tags[0]['social_media_image']:
            social_media_image_url = change_http_to_https(
                request.build_absolute_uri(
                    current_meta_tags[0]['social_media_image']
                )
            )
        else:
            social_media_image_url = change_http_to_https(
                request.build_absolute_uri(
                    '/media/{}'.format(current_meta_tags[0]['social_media_image'])
                )
            )

        google_logo_url = ''
        if '/static/' in current_meta_tags[0]['google_logo']:
            google_logo_url = change_http_to_https(
                request.build_absolute_uri(
                    current_meta_tags[0]['google_logo']
                )
            )
        else:
            google_logo_url = change_http_to_https(
                request.build_absolute_uri(
                    '/media/{}'.format(current_meta_tags[0]['google_logo'])
                )
            )

        return {
            'path': path,
            'current_url': current_url,
            'current_domain': current_domain,
            'google_description': current_meta_tags[0]['google_description'],
            'social_media_site_name': current_meta_tags[0]['social_media_site_name'],
            'social_media_type': current_meta_tags[0]['social_media_type'],
            'social_media_title': current_meta_tags[0]['social_media_title'],
            'social_media_description': current_meta_tags[0]['social_media_description'],
            'social_media_image': social_media_image_url,
            'google_type': current_meta_tags[0]['google_type'],
            'google_name': current_meta_tags[0]['google_name'],
            'google_alterantive_name': current_meta_tags[0]['google_alterantive_name'],
            'google_description': current_meta_tags[0]['google_description'],
            'google_logo': google_logo_url,
            'google_telephone': current_meta_tags[0]['google_telephone'],
            'google_address_type': current_meta_tags[0]['google_address_type'],
            'google_address_street': current_meta_tags[0]['google_address_street'],
            'google_address_locality': current_meta_tags[0]['google_address_locality'],
            'google_address_region': current_meta_tags[0]['google_address_region'],
            'google_social_media_facebook': current_meta_tags[0]['google_social_media_facebook'],
            'google_social_media_instagram': current_meta_tags[0]['google_social_media_instagram'],
            'google_social_media_youtube': current_meta_tags[0]['google_social_media_youtube'],
            'google_social_media_tiktok': current_meta_tags[0]['google_social_media_tiktok'],
        }
    else:
        return False
