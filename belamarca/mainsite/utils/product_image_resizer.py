#------------------------------------------#
# Suporte para redimensionamento de imagens
#------------------------------------------#

from io import BytesIO
from PIL import Image
from resizeimage import resizeimage
from django.core.files.images import get_image_dimensions
from django.conf import settings
import os
import hashlib
from genericapp.models import ImagesResized
from unidecode import unidecode


def create_product_image_resizer(instance, model):
    '''
    Esta função recebe a instância, o modelo e os sizes específicos
    das imagens para criação das versões mobile, tablet e desktop
    de cada imagem que estiver com 'image_resize' em alguma parte
    do seu nome de atributo.
    '''

    # Pegando nomes dos campos de imagens e tamanhos recebidos na nova instancia
    # com 'image_resize' e 'image_size' no nome
    image_to_resize_attributes_names = ['p3_image_resize',]
    image_size_attributes_names = ['p3_image_size',]
    model_name = model.__name__

    # Criando uma lista com os field_names atrelados aos seus respectivos sizes
    images_and_sizes_list = []
    for field_name in image_to_resize_attributes_names:
        for field_image_size in image_size_attributes_names:
            field_name_list = field_name.split('_')
            del(field_name_list[-1])
            del(field_name_list[-1])
            field_name_list = '_'.join(field_name_list)

            field_size_list = field_image_size.split('_')
            del(field_size_list[-1])
            del(field_size_list[-1])
            field_size_list = '_'.join(field_size_list)

            if(field_name_list == field_size_list):
                field_size_value = getattr(instance, field_image_size)
                final_size = tuple(field_size_value.split('x'))
                images_and_sizes_list.append(tuple([field_name, final_size]))

    # Laço de repetição para redimensionamento das imagens do 'instance' recebido
    for field_name in image_to_resize_attributes_names:
        # Pegando as imagens novas no field_name
        instace_image = getattr(instance, field_name)

        if ImagesResized.objects.filter(model_id=instance.id, model_name=model_name, field_name=field_name).exists():
            old_resized_images = ImagesResized.objects.filter(
                model_id=instance.id, model_name=model_name, field_name=field_name)

            # Limpando thumbnails para cadastro do novo
            # redimensionamento da imagem
            for image in old_resized_images:
                clean_unusable_thumbnails(image.image_mobile)
                clean_unusable_thumbnails(image.image_tablet)
                clean_unusable_thumbnails(image.image_desktop)

            # Se já existirem imagens refatoradas elas devem ser excluídas
            old_resized_images.delete()

        if instace_image != None:
            # Atribuindo os tamanhos para desktop, tablet e mobile
            output_size_desktop = None
            output_size_tablet = None
            output_size_mobile = None

            for size in images_and_sizes_list:
                if size[0] == field_name:
                    image_size = {
                        'widht': int(size[1][0]),
                        'length': int(size[1][1]),
                    }

                    output_size_desktop = tuple([image_size['widht'], image_size['length']])
                    output_size_tablet = tuple(
                        [int(image_size['widht']/2), int(image_size['length']/2)])
                    output_size_mobile = tuple(
                        [int((image_size['widht']/2)/2), int((image_size['length']/2)/2)])


            image_name = instance.p3_image_resize.name.split('/')[1]

            rename = '{}{}{}{}'.format(
                model_name,
                instance.id,
                field_name,
                image_name
            )

            print(instace_image.name)

            rename = hash_image_name(rename)
            rename = '{}-{}'.format(unidecode(image_name.replace(" ", "-")), rename)

            # Em ambos os casos fazemos o redimensionamento e cadastramos novamente
            image_desktop = image_optimizer(
                image_data=instace_image.file,
                output_size=output_size_desktop,
                rename=rename,
                device='desktop'
            )

            image_tablet = image_optimizer(
                image_data=instace_image.file,
                output_size=output_size_tablet,
                rename=rename,
                device='tablet'
            )

            image_mobile = image_optimizer(
                image_data=instace_image.file,
                output_size=output_size_mobile,
                rename=rename,
                device='mobile'
            )

            image_resized = ImagesResized(
                image_mobile=image_mobile,
                image_tablet=image_tablet,
                image_desktop=image_desktop,
                model_name=model_name,
                model_id=instance.id,
                field_name=field_name,
            )
            image_resized.save()


def delete_product_image_resizer(instance, model):
    '''
    Esta função recebe a instância e o modelo específicos para
    exclusão das versões mobile, tablet e desktop das imagens
    redimensionadas para a instância que foi removida. Ela é
    importante para evitar o acumulo de arquivos inutilizados
    no diretório de 'media' do projeto.
    '''

    # Pegando nomes dos campos de imagens recebidas na instancia
    # que foi excluída e que tenham 'image_resize' em seus nomes
    # de atributo.
    image_to_delete_attributes_names = ['p3_image_resize']

    # Pegando nome do modelo específico para busca das imagens redimensionadas
    model_name = model.__name__

    for field_name in image_to_delete_attributes_names:
        if ImagesResized.objects.filter(model_id=instance.id, model_name=model_name, field_name=field_name).exists():
            old_resized_images = ImagesResized.objects.filter(
                model_id=instance.id, model_name=model_name, field_name=field_name)

            for image in old_resized_images:
                clean_unusable_thumbnails(image.image_mobile)
                clean_unusable_thumbnails(image.image_tablet)
                clean_unusable_thumbnails(image.image_desktop)

            # Excluindos as imagens inutilizadas
            old_resized_images.delete()


class ProportionalRedemption:
    def __init__(self, width, height, limit_width, limit_height):
        self.width = width
        self.height = height
        self.limit_width = limit_width
        self.limit_height = limit_height

    def proportional_redemption(self):
        '''
        Return width and height without reach limit_width or limit_height
        Thus rezise the dimension of the image without affecting their quality
        Hint: Always the dimensions of the images must be greater than their limits to not lose their quality
        '''
        width_original = self.width
        height_original = self.height

        if self.height > self.limit_height and self.width > self.limit_width:
            self.while_two_biggest()
        elif self.height < self.limit_height and self.width < self.limit_width:
            self.while_two_minors()
        elif self.height < self.limit_height:
            self.while_only_height_biggest()
        elif self.width < self.limit_width:
            self.while_only_width_biggest()

        if self.width == self.limit_width:
            self.height = round(
                (self.width * height_original) / width_original)
        else:
            self.width = round(
                (self.height * width_original) / height_original)

        return (self.width, self.height)

    def while_two_biggest(self):
        while self.height > self.limit_height and self.width > self.limit_width:
            self.height -= 1
            self.width -= 1

    def while_two_minors(self):
        while self.height < self.limit_height and self.width < self.limit_width:
            self.height += 1
            self.width += 1

    def while_only_height_biggest(self):
        while self.height < self.limit_height:
            self.height += 1
            self.width += 1

    def while_only_width_biggest(self):
        while self.width < self.limit_width:
            self.height += 1
            self.width += 1


def get_file_name(file_name):
    '''
    Return file name without extension
    '''
    return str(file_name).split('.')[0]


def get_image_extension(image):
    '''
    Return image extension
    '''
    new_image = image.get_format_mimetype()
    image_format = image.format

    if new_image.split('/')[-1].lower() != 'webp':
        image_format = 'WEBP'

    return image_format


def image_optimizer(image_data, output_size=None, rename=None, device=None):

    if not os.path.isfile(os.path.join(settings.MEDIA_ROOT, str(image_data))):
        return ''

    width, height = get_image_dimensions(image_data)
    output_width, output_height = output_size

    pr_image = ProportionalRedemption(
        width, height, output_width, output_height)
    output_size = pr_image.proportional_redemption()

    with open(os.path.join(settings.MEDIA_ROOT, str(image_data)), 'rb') as f:
        image = Image.open(BytesIO(f.read()))

    extension = get_image_extension(image)

    BACKGROUND_TRANSPARENT = (255, 255, 255, 0)

    if output_size is not None:
        image = resizeimage.resize_cover(image, output_size, validate=False)
        output_image = Image.new('RGBA', output_size, BACKGROUND_TRANSPARENT)
        output_image_center = (int((output_size[0] - image.size[0]) / 2),
                               int((output_size[1] - image.size[1]) / 2))
        output_image.paste(image, output_image_center)
    else:
        output_image = image

    # output_image = output_image.convert('RGB')

    if rename is not None:
        renamed_image = f'{rename}-{device}.{extension.lower()}'

    output_image.seek(0)
    output_image.save(os.path.join(settings.MEDIA_ROOT, renamed_image),
                      format=extension, optimize=True, quality=90)

    return renamed_image


def hash_image_name(image_name):
    md5 = hashlib.md5()
    md5.update(image_name.encode('utf-8'))

    return md5.hexdigest()


def clean_unusable_thumbnails(image_path):
    file_path = os.path.join(settings.MEDIA_ROOT, str(image_path))
    if os.path.isfile(file_path):
        os.remove(file_path)


def resized_images(model_name, model_objects):
    '''
    Função para retornar imagens de um modelo.
    Usada apenas em modelos com uma imagem.
    '''
    for i, model in enumerate(model_objects):
        if ImagesResized.objects.filter(model_id=model.id, model_name=model_name).exists():
            resized_images = ImagesResized.objects.filter(
                model_id=model.id,
                model_name=model_name)

            model_objects[i].resized_images = resized_images[0]
    return model_objects
