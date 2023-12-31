from imp import acquire_lock
from django.shortcuts import render
from django.http import JsonResponse
from mainsite.utils.mail_jet_sender import send_simple_email
from validate_email import validate_email
import csv
from django.core.files import File
from django.core.files.base import ContentFile
from django.templatetags.static import static
from django.views.generic import ListView, DetailView
from genericapp.models import ImagesResized
import ast

from django.conf import settings

from unidecode import unidecode

from .models import (
    Product,
    Category,
    Subcategory,
    Attribute,
    AttributeOption,
    ProductPrice,
    ProductImage,
    Disponibility,
)

from seoapp.models import (
    SeoMetaTags,
    GoogleProductMetaTag,
)


def get_products_from_csv(request):

    file = open('static/csv/products.csv')

    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)

    products = str(rows).split('[')
    # final_products = list(products)

    x=0
    for product in products:
        #print(x)
        datas = product.split(';')

        codigo = None
        produto = None
        descricao = None
        ficha_tecnica = None
        categoria = None
        subcategoria = None
        atributos_tipo = None
        atributos_cor = None
        atributos_estampa = None
        atributos_tamanho = None
        atributos_tecido = None
        price = None
        disponibilidade = None
        imagens_nome = None
        slug = None # Concatenar: produto(sem ascento e minúculo)-codigo-tecido

        if x > 1: # Regra para ignorar o cabeçalho do CSV
            y = 0
            for data in datas:
                data = ((data.replace("'", '')).replace("]]", '')).replace("],", '')

                if y < 14:
                    if y == 0:
                        codigo = data
                    if y == 1:
                        produto = data
                    if y == 2:
                        descricao = data
                    if y == 3:
                        ficha_tecnica = data
                    if y == 4:
                        categorias = data
                    if y == 5:
                        subcategorias = data
                    if y == 6:
                        atributos_tipo = data
                    if y == 7:
                        atributos_cor = data
                    if y == 8:
                        atributos_estampa = data
                    if y == 9:
                        atributos_tamanho = data
                    if y == 10:
                        atributos_tecido = data
                    if y == 11:
                        price = data
                    if y == 12:
                        disponibilidade = data
                    if y == 13:
                        imagens_nome = data
                    if y == 14:
                        slug = data
                y += 1

            # Tratando campos necessários

            # Listas para armazenar os objetos finais de cada categiria, subcategoria e atributos
            final_categorias = []
            final_subcategorias = []
            final_atributos_tipo = []
            final_atributos_cor = []
            final_atributos_estampa = []
            final_atributos_tamanho = []
            final_atributos_tecido = []
            final_imagens_nome = []

            # Tratando categoria para cadastrar caso não exista
            categorias_list = categorias.split(',')

            for categoria in categorias_list:
                if categoria != '-' and categoria != '':
                    categoria_obj = Category.objects.filter(name=categoria.strip())
                    if categoria_obj.count() == 0:
                        # Criar a categoria caso ela não exista
                        new_category = Category(
                            name=categoria,
                            disp='disponivel',
                        )
                        new_category.save()
                        categoria_obj = Category.objects.filter(name=categoria)

                        if categoria_obj.count() > 0:
                            final_categorias.append(categoria_obj[0])
                    else:
                        final_categorias.append(categoria_obj[0])

            # Tratando subcategoria para cadastrar caso não exista
            subcategorias_list = subcategorias.split(',')

            for subcategoria in subcategorias_list:
                if subcategoria != '-' and subcategoria != '':
                    subcategoria_obj = Subcategory.objects.filter(name=subcategoria.strip())
                    if subcategoria_obj.count() == 0:
                        # Criar a categoria caso ela não exista
                        new_subcategory = Subcategory(
                            name=subcategoria,
                            disp='disponivel',
                        )
                        new_subcategory.save()
                        subcategoria_obj = Subcategory.objects.filter(name=subcategoria)

                        if subcategoria_obj.count() > 0:
                            final_subcategorias.append(subcategoria_obj[0])
                    else:
                        final_subcategorias.append(subcategoria_obj[0])

            # Verificando se atributos já existem e cadastrando caso não existam
            attributes_names_list = [
                'Tipo', # Estampado ou Liso
                'Cor',
                'Tamanho',
                'Estampa',
                'Tecído',
            ]

            attributes_obj_list = []

            for attribute_name in attributes_names_list:
                attribute_obj = Attribute.objects.filter(name=attribute_name)

                if attribute_obj.count() == 0:
                    if attribute_name == 'Tipo':
                        is_color = False
                        is_text = True
                        is_image = False
                    if attribute_name == 'Cor':
                        is_color = True
                        is_text = False
                        is_image = False
                    elif attribute_name == 'Tamanho':
                        is_color = False
                        is_text = True
                        is_image = False
                    elif attribute_name == 'Estampa':
                        is_color = False
                        is_text = False
                        is_image = True
                    elif attribute_name == 'Tecído':
                        is_color = False
                        is_text = False
                        is_image = True

                    new_attribute = Attribute(
                        name=attribute_name,
                        is_text=is_text,
                        is_image=is_image,
                        is_color=is_color,
                        disp='disponivel',
                    )

                    new_attribute.save()

                    attribute_obj = Attribute.objects.filter(name=attribute_name)

                attributes_obj_list.append({
                    'name': attribute_name,
                    'object': attribute_obj
                })

            # Recuperar ou cadastrar os "AttributesOptions" desse tipo de "Attributes"

            # Tratando "atributos_tipo" para cadastrar caso não exista
            # Tratando "atributos_cor" para cadastrar caso não exista
            # Tratando "atributos_estampa" para cadastrar caso não exista
            # Tratando "atributos_tamanho" para cadastrar caso não exista
            # Tratando "atributos_tecido" para cadastrar caso não exista

            for attribute_obj_and_name in attributes_obj_list:
                attribute_name = attribute_obj_and_name.get('name')
                attribute_obj = attribute_obj_and_name.get('object')[0]

                if attribute_name == 'Tipo': #final_atributos_tipo
                    atributos_tipo_list = atributos_tipo.split(',')

                    for tipo in atributos_tipo_list:
                        if tipo != '-' and tipo != '':
                            tipo_obj = AttributeOption.objects.filter(
                                attribute=attribute_obj,
                                name=tipo.strip(),
                            )

                            if tipo_obj.count() == 0:
                                    # Adicionar nova cor caso ela não exista
                                    new_attribute_option = AttributeOption(
                                        attribute=attribute_obj,
                                        name=tipo.strip(),
                                        text=tipo.strip(),
                                    )
                                    new_attribute_option.save()

                                    tipo_obj = AttributeOption.objects.filter(
                                        attribute=attribute_obj,
                                        name=tipo.strip(),
                                    )

                                    if tipo_obj.count() > 0:
                                        final_atributos_tipo.append(tipo_obj[0])
                            else:
                                final_atributos_tipo.append(tipo_obj[0])
                if attribute_name == 'Cor':
                    atributos_cor_list = atributos_cor.split(',')

                    for cor in atributos_cor_list:
                        cor_obj = AttributeOption.objects.filter(
                            attribute=attribute_obj,
                            name=cor.strip(),
                        )

                        if cor != '-' and cor != '':
                            if cor_obj.count() == 0:
                                # Pegar hexadecimal da cor no setings "PRODUCSTS_COLORS_HEXADECIMAL"
                                def get_hexadecimal_for_option(cor):
                                    for option, hexadecimal in settings.PRODUCSTS_COLORS_HEXADECIMAL:
                                        if option == cor.strip():
                                            return hexadecimal

                                color_hexadecimal = get_hexadecimal_for_option(cor)

                                # Adicionar nova cor caso ela não exista
                                new_attribute_option = AttributeOption(
                                    attribute=attribute_obj,
                                    name=cor.strip(),
                                    color=color_hexadecimal,
                                )
                                new_attribute_option.save()

                                cor_obj = AttributeOption.objects.filter(
                                    attribute=attribute_obj,
                                    name=cor.strip(),
                                )

                                if cor_obj.count() > 0:
                                    final_atributos_cor.append(cor_obj[0])
                            else:
                                final_atributos_cor.append(cor_obj[0])
                if attribute_name == 'Estampa': #final_atributos_estampa
                    atributos_estampa_list = atributos_estampa.split(',')

                    for estampa in atributos_estampa_list:
                        estampa_obj = AttributeOption.objects.filter(
                            attribute=attribute_obj,
                            name=estampa.strip(),
                        )
                        if estampa != '-' and estampa != '':
                            if estampa_obj.count() == 0:
                                    # Adicionar nova cor caso ela não exista
                                    new_attribute_option = AttributeOption(
                                        attribute=attribute_obj,
                                        name=estampa.strip(),
                                    )

                                    # Pegar nome da imagem da estampa no setings "PRODUCSTS_PRINTS_IMAGES"
                                    def get_image_name_for_print(estampa):
                                        for option, image_name in settings.PRODUCSTS_PRINTS_IMAGES:
                                            if option == estampa.strip():
                                                return image_name

                                    print_image_name = get_image_name_for_print(estampa)

                                    if print_image_name != None:
                                        print_image_path = 'products_images/prints/{}'.format(print_image_name)

                                        new_attribute_option.p2_image_image_resize = print_image_path

                                    new_attribute_option.save()

                                    estampa_obj = AttributeOption.objects.filter(
                                        attribute=attribute_obj,
                                        name=estampa.strip(),
                                    )

                                    if estampa_obj.count() > 0:
                                        final_atributos_estampa.append(estampa_obj[0])
                            else:
                                final_atributos_estampa.append(estampa_obj[0])
                if attribute_name == 'Tamanho': #final_atributos_tamanho
                    atributos_tamanho_list = atributos_tamanho.split(',')

                    for tamanho in atributos_tamanho_list:
                        if tamanho != '-' and tamanho != '':
                            tamanho_obj = AttributeOption.objects.filter(
                                attribute=attribute_obj,
                                name=tamanho.strip(),
                            )

                            if tamanho_obj.count() == 0:
                                    # Adicionar nova cor caso ela não exista
                                    new_attribute_option = AttributeOption(
                                        attribute=attribute_obj,
                                        name=tamanho.strip(),
                                        text=tamanho.strip(),
                                    )
                                    new_attribute_option.save()

                                    tamanho_obj = AttributeOption.objects.filter(
                                        attribute=attribute_obj,
                                        name=tamanho.strip(),
                                    )

                                    if tamanho_obj.count() > 0:
                                        final_atributos_tamanho.append(tamanho_obj[0])
                            else:
                                final_atributos_tamanho.append(tamanho_obj[0])
                if attribute_name == 'Tecído': #final_atributos_tecido
                    atributos_tecido_list = atributos_tecido.split(',')

                    for tecido in atributos_tecido_list:
                        if tecido != '-' and tecido != '':
                            tecido_obj = AttributeOption.objects.filter(
                                attribute=attribute_obj,
                                name=tecido.strip(),
                            )

                            if tecido_obj.count() == 0:
                                    # Adicionar nova cor caso ela não exista
                                    new_attribute_option = AttributeOption(
                                        attribute=attribute_obj,
                                        name=tecido.strip(),
                                        text=tecido.strip(),
                                    )
                                    new_attribute_option.save()

                                    tecido_obj = AttributeOption.objects.filter(
                                        attribute=attribute_obj,
                                        name=tecido.strip(),
                                    )

                                    if tecido_obj.count() > 0:
                                        final_atributos_tecido.append(tecido_obj[0])
                            else:
                                final_atributos_tecido.append(tecido_obj[0])

            # Tratando imagens para cadastrar caso não exista
            imagens_nome_list = imagens_nome.split(',')

            for imagem_nome in imagens_nome_list:
                if imagem_nome != '-' and imagem_nome != '':
                    final_imagens_nome.append(imagem_nome.strip())

             # Tratando slug
            produto_parte = unidecode(produto.lower().replace(" ", "-").replace(")", "").replace("(", ""))
            tecido_parte = unidecode(atributos_tecido.lower().replace(" ", "-").replace(")", "").replace("(", ""))
            codigo_parte = codigo.lower()
            slug = '{}-{}-{}'.format(produto_parte, tecido_parte, codigo_parte)

            if codigo != '':
                print('---------------------------------')
                print(codigo)
                print(produto)
                print(descricao)
                print(ficha_tecnica)
                print(price)
                print(disponibilidade)
                print(imagem_nome)
                print(slug)
                print(final_categorias)
                print(final_subcategorias)
                print(final_atributos_tipo)
                print(final_atributos_cor)
                print(final_atributos_estampa)
                print(final_atributos_tamanho)
                print(final_atributos_tecido)

                # Verificando se o produto não existe através do "slug"
                # e apagando caso exista para adicionar novamente

                product_obj = Product.objects.filter(
                    slug=slug,
                )

                if product_obj.count() > 0:
                    product_obj[0].delete()

                # Cadastrando o novo produto
                new_product = Product(
                    code=codigo,
                    name=produto,
                    description=descricao,
                    datasheet=ficha_tecnica,
                    slug=slug,
                )
                new_product.save()

                # Cadastrando preço do produto
                if price != '' and price != '-':
                    product_price = ProductPrice(
                        id_product=new_product,
                        price=price,
                    )
                    product_price.save()

                # Cadastrando categorias, subcategorias e atributos do produto
                for obj in final_categorias:
                    new_product.category.add(obj)

                for obj in final_subcategorias:
                    new_product.subcategory.add(obj)

                for obj in final_atributos_tipo:
                    new_product.attribute_options.add(obj)

                for obj in final_atributos_cor:
                    new_product.attribute_options.add(obj)

                for obj in final_atributos_estampa:
                    new_product.attribute_options.add(obj)

                for obj in final_atributos_tamanho:
                    new_product.attribute_options.add(obj)

                for obj in final_atributos_tecido:
                    new_product.attribute_options.add(obj)

                # Cadastrando imagens do produto
                for image_name in final_imagens_nome:
                    if image_name != '' and image_name != '-':
                        image_path = 'products_images/{}'.format(image_name)

                        new_product_image = ProductImage(
                            product=new_product,
                            alt=new_product.name,
                        )
                        new_product_image.p3_image_resize = image_path
                        new_product_image.save()

                # Cadastrando SEO do produto
                seo_meta_tag = SeoMetaTags.objects.create(
                    path='/produto/{}/'.format(slug),
                    title='{} | Bela Marca'.format(produto),
                    description=descricao
                )
                seo_meta_tag.save()

                try:
                    google_product_meta_tag = GoogleProductMetaTag.objects.get(seo_meta_tags=seo_meta_tag)

                    google_product_meta_tag.google_product_code = codigo
                    google_product_meta_tag.google_product_name = '{} | Bela Marca'.format(produto)
                    google_product_meta_tag.google_product_description = descricao
                    google_product_meta_tag.google_product_price = price

                    if len(final_imagens_nome) > 0:
                        seo_image_path = 'products_images/{}'.format(final_imagens_nome[0])
                        seo_meta_tag.image = seo_image_path
                        seo_meta_tag.save()

                        google_product_meta_tag.google_product_image = seo_image_path

                    google_product_meta_tag.save()
                except GoogleProductMetaTag.DoesNotExist:
                    google_product_meta_tag = GoogleProductMetaTag.objects.create(
                        seo_meta_tags=seo_meta_tag,
                        google_product_code=codigo,
                        google_product_name='{} | Bela Marca'.format(produto),
                        google_product_description=descricao,
                        google_product_price=price
                    )

                    if len(final_imagens_nome) > 0:
                        seo_image_path = 'products_images/{}'.format(final_imagens_nome[0])
                        seo_meta_tag.image = seo_image_path
                        seo_meta_tag.save()

                        google_product_meta_tag.google_product_image = seo_image_path

                    google_product_meta_tag.save()

        x += 1
    print('---------------------------------')
    print('Produtos, categorias, atributos e preços cadastrados com sucesso!')

    codigo = '1'
    produto = '1'
    descricao = '1'
    ficha_tecnica = '1'
    categoria = '1'
    subcategoria = '1'
    atributos = '1'

    context = {
        'codigo': codigo,
        'produto': produto,
        'descricao': descricao,
        'ficha_tecnica': ficha_tecnica,
        'categoria': categoria,
        'subcategoria': subcategoria,
        'atributos': atributos,
    }

    return render(request, "productapp/get_products_from_csv.html", context=context)
    #return JsonResponse(context)

def get_products_images_from_csv(request):

    file = open('static/csv/products_images.csv')

    #print(type(file))

    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)

    products = str(rows).split('[')
    x=0
    for product in products:
        #print(x)
        datas = product.split(';')

        code = None
        product_image = None

        if x > 1:
            y = 0
            for data in datas:
                data = ((data.replace("'", '')).replace("]]", '')).replace("],", '')
                if y < 13:
                    if y == 0:
                        code = data
                    if y == 1:
                        product_image = data.strip()

                    if product_image != None:

                        product = Product.objects.filter(code=code).get()
                        image_path = 'products_images/{}'.format(product_image)

                        new_product_image = ProductImage(
                            product=product,
                            alt=product.name,
                        )
                        new_product_image.p3_image_resize = image_path
                        new_product_image.save()

                y += 1

        x += 1
    print('---------------------------------')
    print('Imagens de produtos cadastradas com sucesso!')

    code = '1'

    context = {
        'code': code,
    }

    return render(request, "productapp/get_products_images_from_csv.html", context=context)

class ProductDetailView(DetailView):
    model = Product
    template_name = "productapp/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        product_price = ProductPrice.objects.filter(id_product=product).get()

        product_attribute_options = Product.objects.get(pk=product.id).attribute_options.all()

        garment_size = []
        garment_type = []
        garment_color = []
        garment_print = []
        garment_material = []

        for attribute_option in product_attribute_options:
            if attribute_option.attribute.name == 'Tamanho':
                garment_size.append(attribute_option.text)

            if attribute_option.attribute.name == 'Tipo':
                garment_type.append(attribute_option.text)

            if attribute_option.attribute.name == 'Cor':
                garment_color.append(attribute_option.color)

            if attribute_option.attribute.name == 'Estampa':

                if attribute_option.p2_image_image_resize != None:
                    model_name = AttributeOption.__name__
                    image_id = attribute_option.id
                    resized_images = None

                    if ImagesResized.objects.filter(model_id=image_id, model_name=model_name).exists():
                        resized_images = ImagesResized.objects.filter(
                            model_id=image_id, model_name=model_name
                        )

                        garment_print.append({
                            'image': resized_images[0].image_desktop.url,
                            'alt': attribute_option.name,
                        })
            if attribute_option.attribute.name == 'Tecído':
                garment_material.append(attribute_option.text)

        context.update({
            'price': "{:.2f}".format(product_price.price),
            'garment_size': garment_size,
            'garment_type': garment_type,
            'garment_color': garment_color,
            'garment_print': garment_print,
            'garment_material': garment_material,
        })
        return context


# class ProductListView(ListView):
#     model = Product
#     template_name = "productapp/product_list.html"

def ProductListView(request):
    '''
    Forma de receber as informações por get:
    /produtos/?categories=[1]&sizes=[4,5,6,7]&types=[4,5,6,7]&colors=[1]&prints=[9]&materials=[4,5,6,7]
    '''
    categories = request.GET.get('categories', '')
    sizes = request.GET.get('sizes', '')
    types = request.GET.get('types', '')
    colors = request.GET.get('colors', '')
    prints = request.GET.get('prints', '')
    materials = request.GET.get('materials', '')

    if categories is not '':
        categories = ast.literal_eval(categories)
    else:
        categories = []

    if sizes is not '':
        sizes = ast.literal_eval(sizes)
    else:
        sizes = []

    if types is not '':
        types = ast.literal_eval(types)
    else:
        types = []

    if colors is not '':
        colors = ast.literal_eval(colors)
    else:
        colors = []

    if prints is not '':
        prints = ast.literal_eval(prints)
    else:
        prints = []

    if materials is not '':
        materials = ast.literal_eval(materials)
    else:
        materials = []

    products = []

    # Pegar o obj de cada AttributeOption para fazer a filtragem
    final_categories = []
    final_attribute_options = []
    if (
        len(categories) > 0 and
        len(sizes) == 0 and
        len(types) == 0 and
        len(colors) == 0 and
        len(prints) == 0 and
        len(materials) == 0
    ):
        for category in categories:
            # Atribuindo os ids das Category na lista 'final_categories'
            final_categories.append(category)

        products = Product.objects.filter(
            category__id__in=final_categories,
            productimage__isnull=False, # Apenas produtos que tenham imagem
            productprice__price__gt=0, # Apenas produtos com preço > 0
            disp=Disponibility.DISPONIVEL
        ).order_by('-id')
    elif (
        len(categories) == 0 and
        len(sizes) > 0 or
        len(types) > 0 or
        len(colors) > 0 or
        len(prints) > 0 or
        len(materials) > 0
    ):
        if len(sizes) > 0:
            for size in sizes:
                # Atribuindo os ids dos AttributeOption na lista 'final_attribute_options'
                final_attribute_options.append(size)

        if len(types) > 0:
            for type in types:
                # Atribuindo os ids dos AttributeOption na lista 'final_attribute_options'
                final_attribute_options.append(type)

        if len(colors) > 0:
            for color in colors:
                # Atribuindo os ids dos AttributeOption na lista 'final_attribute_options'
                final_attribute_options.append(color)

        if len(prints) > 0:
            for print_ in prints:
                # Atribuindo os ids dos AttributeOption na lista 'final_attribute_options'
                final_attribute_options.append(print_)

        if len(materials) > 0:
            for material in materials:
                # Atribuindo os ids dos AttributeOption na lista 'final_attribute_options'
                final_attribute_options.append(material)

        products = Product.objects.filter(
            attribute_options__id__in=final_attribute_options,
            productimage__isnull=False, # Apenas produtos que tenham imagem
            productprice__price__gt=0, # Apenas produtos com preço > 0
            disp=Disponibility.DISPONIVEL
        ).order_by('-id')
    elif (
        len(categories) > 0 or
        len(sizes) > 0 or
        len(types) > 0 or
        len(colors) > 0 or
        len(prints) > 0 or
        len(materials) > 0
    ):
        #Pegando produtos de cada filtro selecionado
        if len(categories) > 0:
            for category in categories:
                # Atribuindo os ids das Category na lista 'final_categories'
                final_categories.append(category)

        if len(sizes) > 0:
            for size in sizes:
                # Atribuindo os ids dos AttributeOption na lista 'final_attribute_options'
                final_attribute_options.append(size)

        if len(types) > 0:
            for type in types:
                # Atribuindo os ids dos AttributeOption na lista 'final_attribute_options'
                final_attribute_options.append(type)

        if len(colors) > 0:
            for color in colors:
                # Atribuindo os ids dos AttributeOption na lista 'final_attribute_options'
                final_attribute_options.append(color)

        if len(prints) > 0:
            for print_ in prints:
                # Atribuindo os ids dos AttributeOption na lista 'final_attribute_options'
                final_attribute_options.append(print_)

        if len(materials) > 0:
            for material in materials:
                # Atribuindo os ids dos AttributeOption na lista 'final_attribute_options'
                final_attribute_options.append(material)

        products = Product.objects.filter(
            category__id__in=final_categories,
            attribute_options__id__in=final_attribute_options,
            productimage__isnull=False, # Apenas produtos que tenham imagem
            productprice__price__gt=0, # Apenas produtos com preço > 0
            disp=Disponibility.DISPONIVEL
        ).order_by('-id')
    else:
        products = Product.objects.filter(
            productimage__isnull=False, # Apenas produtos que tenham imagem
            productprice__price__gt=0, # Apenas produtos com preço > 0
            disp=Disponibility.DISPONIVEL
        ).order_by('-id')

    unique_product_ids = set()
    unique_products = []

    for product in products:
        if product.id not in unique_product_ids:
            # Pegando preço dos produtos
            product_price = ProductPrice.objects.filter(id_product=product).get()
            product.price = "{:.2f}".format(product_price.price)

            # Inserindo produtos a lista única final
            unique_product_ids.add(product.id)
            unique_products.append(product)

    context = {
        'products': unique_products,
    }

    return render(request, "productapp/product_list.html", context=context)

def ProductHomeView(request):

    context = {
        'teste': 'teste do dandan',
    }

    return render(request, "productapp/product_home.html", context=context)