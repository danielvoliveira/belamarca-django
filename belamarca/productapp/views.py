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
                        atributos_cor = data
                    if y == 7:
                        atributos_estampa = data
                    if y == 8:
                        atributos_tamanho = data
                    if y == 9:
                        atributos_tecido = data
                    if y == 10:
                        price = data
                    if y == 11:
                        disponibilidade = data
                    if y == 12:
                        imagens_nome = data
                    if y == 13:
                        slug = data
                y += 1

            # Tratando campos necessários

            # Listas para armazenar os objetos finais de cada categiria, subcategoria e atributos
            final_categorias = []
            final_subcategorias = []
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
                            disp=disponibilidade,
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
                            disp=disponibilidade,
                        )
                        new_subcategory.save()
                        subcategoria_obj = Subcategory.objects.filter(name=subcategoria)

                        if subcategoria_obj.count() > 0:
                            final_subcategorias.append(subcategoria_obj[0])
                    else:
                        final_subcategorias.append(subcategoria_obj[0])

            # Verificando se atributos já existem e cadastrando caso não existam
            attributes_names_list = [
                'Cor',
                'Tamanho',
                'Estampa',
                'Tecído',
            ]

            attributes_obj_list = []

            for attribute_name in attributes_names_list:
                attribute_obj = Attribute.objects.filter(name=attribute_name)

                if attribute_obj.count() == 0:
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
                        disp=disponibilidade,
                    )

                    new_attribute.save()

                    attribute_obj = Attribute.objects.filter(name=attribute_name)

                attributes_obj_list.append({
                    'name': attribute_name,
                    'object': attribute_obj
                })

            # Recuperar ou cadastrar os "AttributesOptions" desse tipo de "Attributes"

            # Tratando "atributos_cor" para cadastrar caso não exista
            # Tratando "atributos_estampa" para cadastrar caso não exista
            # Tratando "atributos_tamanho" para cadastrar caso não exista
            # Tratando "atributos_tecido" para cadastrar caso não exista

            for attribute_obj_and_name in attributes_obj_list:
                attribute_name = attribute_obj_and_name.get('name')
                attribute_obj = attribute_obj_and_name.get('object')[0]

                if attribute_name == 'Cor':
                    atributos_cor_list = atributos_cor.split(',')

                    for cor in atributos_cor_list:
                        cor_obj = AttributeOption.objects.filter(
                            attribute=attribute_obj,
                            name=cor.strip(),
                        )

                        if cor != '-' and cor != '':
                            if cor_obj.count() == 0:
                                    # Adicionar nova cor caso ela não exista
                                    new_attribute_option = AttributeOption(
                                        attribute=attribute_obj,
                                        name=cor.strip(),
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
                # print('---------------------------------')
                # print(codigo)
                # print(produto)
                # print(descricao)
                # print(ficha_tecnica)
                # print(price)
                # print(disponibilidade)
                # print(imagem_nome)
                # print(slug)
                # print(final_categorias)
                # print(final_subcategorias)
                # print(final_atributos_cor)
                # print(final_atributos_estampa)
                # print(final_atributos_tamanho)
                # print(final_atributos_tecido)

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

        product_attributes = Product.objects.get(pk=product.id).attribute_options.all()

        garment_size = []
        garment_color = []
        garment_print = []
        for atribute in product_attributes:
            if atribute.text != None:
                garment_size.append(atribute.text)

            if atribute.color != None:
                garment_color.append(atribute.color)

            if atribute.p2_image_image_resize_id != None:
                model_name = AttributeOption.__name__
                image_id = atribute.p2_image_image_resize_id
                resized_images = None

                if ImagesResized.objects.filter(model_id=image_id, model_name=model_name).exists():
                    resized_images = ImagesResized.objects.filter(
                        model_id=image_id, model_name=model_name
                    )

                    garment_print.append({
                        'image': resized_images[0].image_desktop.url,
                        'alt': atribute.name,
                    })

        context.update({
            'price': product_price.price,
            'garment_size': garment_size,
            'garment_color': garment_color,
            'garment_print': garment_print,
        })
        return context


# class ProductListView(ListView):
#     model = Product
#     template_name = "productapp/product_list.html"

def ProductListView(request):
    '''
    Forma de receber as informações por get:
    /produtos/?categories=[1]&sizes=[4,5,6,7]&colors=[1]&prints=[9]
    '''
    categories = request.GET.get('categories', '')
    sizes = request.GET.get('sizes', '')
    colors = request.GET.get('colors', '')
    prints = request.GET.get('prints', '')

    if categories is not '':
        categories = ast.literal_eval(categories)
    else:
        categories = []

    if sizes is not '':
        sizes = ast.literal_eval(sizes)
    else:
        sizes = []

    if colors is not '':
        colors = ast.literal_eval(colors)
    else:
        colors = []

    if prints is not '':
        prints = ast.literal_eval(prints)
    else:
        prints = []

    products_categories = []
    products_sizes = []
    products_colors = []
    products_prints = []
    products = []

    if len(categories) > 0 or len(sizes) > 0 or len(colors) > 0 or len(prints):
        #Pegando produtos de cada filtro selecionado
        if len(categories) > 0:
            for category in categories:
                category_obj = Category.objects.filter(id=category).get()

                products_category = Product.objects.filter(
                    category=category_obj
                ).order_by('-id')

                for product in products_category:
                    if product not in products_categories:
                        products_categories.append(product)

        if len(sizes) > 0:
            for size in sizes:
                size_obj = AttributeOption.objects.filter(id=size).get()

                products_size = Product.objects.filter(
                    attribute_options=size_obj
                ).order_by('-id')

                for product in products_size:
                    if product not in products_sizes:
                        products_sizes.append(product)

        if len(colors) > 0:
            for color in colors:
                color_obj = AttributeOption.objects.filter(id=color).get()

                products_color = Product.objects.filter(
                    attribute_options=color_obj
                ).order_by('-id')

                for product in products_color:
                    if product not in products_colors:
                        products_colors.append(product)

        if len(prints) > 0:
            for print_ in prints:
                print_obj = AttributeOption.objects.filter(id=print_).get()

                products_print = Product.objects.filter(
                    attribute_options=print_obj
                ).order_by('-id')

                for product in products_print:
                    if product not in products_prints:
                        products_prints.append(product)

        #Selecionando produtos finais removendo duplicados
        if len(products_categories) > 0:
            for product_category in products_categories:
                if len(products_sizes) > 0 or len(products_colors) > 0 or len(products_prints) > 0:
                    if product_category in products_sizes:
                        if product_category not in products:
                            products.append(product_category)

                    if product_category in products_colors:
                        if product_category not in products:
                            products.append(product_category)

                    if product_category in products_prints:
                        if product_category not in products:
                            products.append(product_category)
                else:
                    products.append(product_category)
        else:
            if len(sizes) > 0:
                for product_size in products_sizes:
                    if product_size not in products:
                        products.append(product_size)

            if len(colors) > 0:
                for product_color in products_colors:
                    if product_color not in products:
                        products.append(product_color)

            if len(prints) > 0:
                for product_print in products_prints:
                    if product_print not in products:
                        products.append(product_print)
    else:
        products = Product.objects.filter().order_by('?')

    for product in products:
        #Pegando preço dos produtos
        product_price = ProductPrice.objects.filter(id_product=product).get()
        product.price = product_price.price

    context = {
        'products': products,
    }

    return render(request, "productapp/product_list.html", context=context)

def ProductHomeView(request):

    context = {
        'teste': 'teste do dandan',
    }

    return render(request, "productapp/product_home.html", context=context)