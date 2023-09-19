from django import template
from django.template.loader import get_template
from cms.models.pagemodel import Page

from seoapp.models import (
    SeoMetaTags,
    GoogleWebSiteMetaTag,
    GoogleCorporationMetaTag,
    GoogleProductListMetaTag,
    GoogleProductMetaTag,
)

# Manter somente quando houver SEO para Produto e Lista de Produto
from productapp.models import (
    Product,
    ProductPrice,
    ProductImage,
)

def change_http_to_https(url):
    if 'http://' in url:
        url = url.replace('http://', 'https://')

    return url

register = template.Library()

@register.inclusion_tag('seoapp/meta_tags.html')
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

        # Recuperando todos os tipos de dados disponíveis para SEO
        current_meta_tags = SeoMetaTags.objects.filter(path=path).values()
        google_web_site_meta_tag = GoogleWebSiteMetaTag.objects.filter(seo_meta_tags__path=path).values()
        google_organization_meta_tag = GoogleCorporationMetaTag.objects.filter(seo_meta_tags__path=path).values()
        google_product_list_meta_tag = GoogleProductListMetaTag.objects.filter(seo_meta_tags__path=path).values()
        google_product_meta_tag = GoogleProductMetaTag.objects.filter(seo_meta_tags__path=path).values()

        if len(current_meta_tags) > 0:
            current_meta_tags = current_meta_tags[0]
        else:
            current_meta_tags = False

        if len(google_web_site_meta_tag) > 0:
            print('Tem Web Site')
            google_web_site_meta_tag = google_web_site_meta_tag[0]
        else:
            google_web_site_meta_tag = False

        if len(google_organization_meta_tag) > 0:
            print('Tem Organization')
            google_organization_meta_tag = google_organization_meta_tag[0]
        else:
            google_organization_meta_tag = False

        if len(google_product_list_meta_tag) > 0:
            print('Tem Lista de Produtos')
            # google_product_list_meta_tag = google_product_list_meta_tag[0]
            google_product_list_meta_tag = GoogleProductListMetaTag()

            # Recuperando Listagem de Produtos
            products = Product.objects.filter(disp='disponivel').order_by('-id')

            # Variável para criação das posições que vão na meta tag
            position = 1
            for product in products:
                #Pegando preço dos produtos
                product_price = ProductPrice.objects.filter(id_product=product).last()
                product.price = product_price.price

                product_image = ProductImage.objects.filter(product_id=product).first()
                if product_image:
                    product_image_url = change_http_to_https(
                        request.build_absolute_uri(
                            product_image.p3_image_resize.url
                        )
                    )

                    product.product_image_url = product_image_url
                else:
                    product.product_image_url = None

                product.position = position
                position += 1

            google_product_list_meta_tag.product_list = products
        else:
            google_product_list_meta_tag = False

        google_product_image_url = '' # Variável para armazenar a url da imagem do produto
        if len(google_product_meta_tag) > 0:
            print('Tem Produto')
            google_product_meta_tag = google_product_meta_tag[0]

            if '/static/' in google_product_meta_tag['google_product_image']:
                google_product_image_url = change_http_to_https(
                    request.build_absolute_uri(
                        google_product_meta_tag['google_product_image']
                    )
                )
            else:
                google_product_image_url = change_http_to_https(
                    request.build_absolute_uri(
                        '/media/{}'.format(google_product_meta_tag['google_product_image'])
                    )
                )
        else:
            google_product_meta_tag = False

        current_meta_tag_image_url = ''
        if '/static/' in current_meta_tags['image']:
            current_meta_tag_image_url = change_http_to_https(
                request.build_absolute_uri(
                    current_meta_tags['image']
                )
            )
        else:
            current_meta_tag_image_url = change_http_to_https(
                request.build_absolute_uri(
                    '/media/{}'.format(current_meta_tags['image'])
                )
            )

        google_logo_url = ''
        if '/static/' in google_organization_meta_tag['google_logo']:
            google_logo_url = change_http_to_https(
                request.build_absolute_uri(
                    google_organization_meta_tag['google_logo']
                )
            )
        else:
            google_logo_url = change_http_to_https(
                request.build_absolute_uri(
                    '/media/{}'.format(google_organization_meta_tag['google_logo'])
                )
            )

        return {
            'path': path,
            'current_url': current_url,
            'current_domain': current_domain,
            'current_meta_tags': current_meta_tags,
            'current_meta_tag_image_url': current_meta_tag_image_url,
            'google_web_site_meta_tag': google_web_site_meta_tag,
            'google_organization_meta_tag': google_organization_meta_tag,
            'google_logo_url': google_logo_url,
            'google_product_list_meta_tag': google_product_list_meta_tag,
            'google_product_meta_tag': google_product_meta_tag,
            'google_product_image_url': google_product_image_url,
            'must_create_seo': must_create_seo,
        }
    else:
        return {
            'must_create_seo': must_create_seo,
        }
