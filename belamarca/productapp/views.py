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

from .models import (
    Product,
    Category,
    Subcategory,
    AttributeOption,
    ProductPrice,
    ProductImage,
)


def get_products_from_csv(request):

    file = open('static/csv/products.csv')

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

        codigo = None
        produto = None
        descricao = None
        ficha_tecnica = None
        categoria = None
        subcategoria = None
        atributos = None
        slug = None
        price = None

        if x > 1:
            y = 0
            for data in datas:
                data = ((data.replace("'", '')).replace("]]", '')).replace("],", '')
                if y < 12:
                    if y == 0:
                        codigo = data
                    if y == 1:
                        produto = data
                    if y == 2:
                        descricao = data
                    if y == 3:
                        ficha_tecnica = data
                    if y == 4:
                        categoria = Category.objects.filter(id=int(data))
                    if y == 5:
                        subcategoria = Subcategory.objects.filter(id=int(data))
                    if y == 6:
                        atributos = AttributeOption.objects.filter(id=int(data))
                    if y == 10:
                        slug = data.replace(" ", "")
                    if y == 11:
                        price = float(data)
                y += 1
            #print('---------------------------------')

            new_product = Product(
                code=codigo,
                name=produto,
                description=descricao,
                datasheet=ficha_tecnica,
                slug=slug,
            )
            new_product.save()
            new_product.category.set(categoria)
            new_product.subcategory.set(subcategoria)
            new_product.attribute_options.set(atributos)

            product_price = ProductPrice(
                id_product=new_product,
                price=price,
            )
            product_price.save()
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