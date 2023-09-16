# Generated by Django 3.2.20 on 2023-09-08 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # ('cms', '0023_auto_20230723_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeoMetaTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(blank=True, editable=False, max_length=300, null=True, verbose_name='Path da página')),
                ('social_media_site_name', models.CharField(blank=True, default='Bela Marca', max_length=100, null=True, verbose_name='Nome do site')),
                ('social_media_type', models.CharField(choices=[('organization', 'Organização/Empresa'), ('website', 'Página Web'), ('blog', 'Página principal do blog')], default='website', max_length=12, verbose_name='Tipo de página')),
                ('social_media_title', models.CharField(blank=True, default='Bela Marca: para mulheres poderosas como você.', help_text='Título para ser exibido quando sua página estiver vinculada. Limite de 100 caracteres.', max_length=100, null=True, verbose_name='Título para Redes Sociais')),
                ('social_media_description', models.TextField(blank=True, default='Bela Marca: para mulheres poderosas como você.', help_text='Lembre-se de que o Facebook exibirá apenas cerca de 300 caracteres de descrição.', max_length=300, null=True, verbose_name='Descrição para Redes Sociais')),
                ('social_media_image', models.ImageField(blank=True, default='../../static/assets/seo_default_image/seo_default_image.jpg', help_text='Tamanho ideal 1200x630px.', null=True, upload_to='seo_images/', verbose_name='Imagem para Redes Sociais e Buscadores')),
                ('google_type', models.CharField(choices=[('Corporation', 'Corporação'), ('Organization', 'Organização')], default='Corporation', editable=False, max_length=12, verbose_name='Tipo de página')),
                ('google_name', models.CharField(blank=True, default='Bela Marca', max_length=100, null=True, verbose_name='Nome do site')),
                ('google_alterantive_name', models.CharField(blank=True, default='Bela Marca: para mulheres poderosas como você.', max_length=200, null=True, verbose_name='Nome alternativo do site')),
                ('google_description', models.TextField(blank=True, default='Bela Marca: para mulheres poderosas como você.', max_length=500, null=True, verbose_name='Descrição do site')),
                ('google_logo', models.ImageField(default='../../static/assets/logo/logo_quadrado_turquesa.png', upload_to='seo_images/')),
                ('google_telephone', models.CharField(blank=True, default='5513997977005', max_length=20, null=True, verbose_name='Telefone para contato')),
                ('google_address_type', models.CharField(blank=True, default='postalAddress', editable=False, max_length=40, null=True, verbose_name='Tipo de endereço')),
                ('google_address_street', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Endereço')),
                ('google_address_locality', models.CharField(blank=True, default='Praia Grande', max_length=100, null=True, verbose_name='Cidade')),
                ('google_address_region', models.CharField(blank=True, default='SP', max_length=100, null=True, verbose_name='Estado')),
                ('google_social_media_facebook', models.URLField(blank=True, default='', max_length=500, null=True, verbose_name='Link do Facebook')),
                ('google_social_media_instagram', models.URLField(blank=True, default='https://www.instagram.com/belamarcastore/', max_length=500, null=True, verbose_name='Link do Instagram')),
                ('google_social_media_youtube', models.URLField(blank=True, default='', max_length=500, null=True, verbose_name='Link do Youtube')),
                ('google_social_media_tiktok', models.URLField(blank=True, default='', max_length=500, null=True, verbose_name='Link do TikTok')),
            ],
            options={
                'verbose_name': 'SEO Meta Tags',
                'verbose_name_plural': 'SEO Meta Tags',
            },
        ),
        migrations.CreateModel(
            name='SeoSinglePagePlugin1',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='seoapp_seosinglepageplugin1', serialize=False, to='cms.cmsplugin')),
                ('metadescription', models.TextField(blank=True, default='Bela Marca: para mulheres poderosas como você.', help_text='Dê a cada página uma meta descrição exclusiva que reflita claramente o valor que a página carrega. Inclua suas palavras-chave mais significativas, para que elas possam ser destacadas. Mas tome cuidado para evitar o excesso de palavras-chave, não faça sua descrição apenas uma combinação de palavras-chave que você está segmentando. Limite de 250 caracteres.', max_length=250, null=True, verbose_name='Descrição da página para buscadores')),
                ('social_media_site_name', models.CharField(blank=True, default='Bela Marca', max_length=100, null=True, verbose_name='Nome do site')),
                ('social_media_type', models.CharField(choices=[('organization', 'Organização/Empresa'), ('website', 'Página Web'), ('blog', 'Página principal do blog')], default='website', max_length=12, verbose_name='Tipo de página')),
                ('social_media_title', models.CharField(blank=True, default='Bela Marca: para mulheres poderosas como você.', help_text='Título para ser exibido quando sua página estiver vinculada. Limite de 100 caracteres.', max_length=100, null=True, verbose_name='Título para Redes Sociais')),
                ('social_media_description', models.TextField(blank=True, default='Bela Marca: para mulheres poderosas como você.', help_text='Lembre-se de que o Facebook exibirá apenas cerca de 300 caracteres de descrição.', max_length=300, null=True, verbose_name='Descrição para Redes Sociais')),
                ('social_media_image', models.ImageField(blank=True, default='../../static/assets/seo_default_image/seo_default_image.jpg', help_text='Tamanho ideal 1200x630px.', null=True, upload_to='seo_images/', verbose_name='Imagem para Redes Sociais e Buscadores')),
                ('google_type', models.CharField(choices=[('Corporation', 'Corporação'), ('Organization', 'Organização')], default='Corporation', editable=False, max_length=12, verbose_name='Tipo de página')),
                ('google_name', models.CharField(blank=True, default='Bela Marca', max_length=100, null=True, verbose_name='Nome do site')),
                ('google_alterantive_name', models.CharField(blank=True, default='Bela Marca: para mulheres poderosas como você.', max_length=200, null=True, verbose_name='Nome alternativo do site')),
                ('google_description', models.TextField(blank=True, default='Bela Marca: para mulheres poderosas como você.', max_length=500, null=True, verbose_name='Descrição do site')),
                ('google_logo', models.ImageField(default='../../static/assets/logo/logo_quadrado_turquesa.png', upload_to='seo_images/')),
                ('google_telephone', models.CharField(blank=True, default='5513997977005', max_length=20, null=True, verbose_name='Telefone para contato')),
                ('google_address_type', models.CharField(blank=True, default='postalAddress', editable=False, max_length=40, null=True, verbose_name='Tipo de endereço')),
                ('google_address_street', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Endereço')),
                ('google_address_locality', models.CharField(blank=True, default='Praia Grande', max_length=100, null=True, verbose_name='Cidade')),
                ('google_address_region', models.CharField(blank=True, default='SP', max_length=100, null=True, verbose_name='Estado')),
                ('google_social_media_facebook', models.URLField(blank=True, default='https://www.facebook.com/acquamotiongramado/', max_length=500, null=True, verbose_name='Link do Facebook')),
                ('google_social_media_instagram', models.URLField(blank=True, default='https://www.instagram.com/belamarcastore/', max_length=500, null=True, verbose_name='Link do Instagram')),
                ('google_social_media_linkedin', models.URLField(blank=True, default='', max_length=500, null=True, verbose_name='Link do Linkedin')),
                ('google_social_media_twitter', models.URLField(blank=True, default='', max_length=500, null=True, verbose_name='Link do Twitter')),
                ('google_social_media_youtube', models.URLField(blank=True, default='', max_length=500, null=True, verbose_name='Link do Youtube')),
                ('google_social_media_tiktok', models.URLField(blank=True, default='', max_length=500, null=True, verbose_name='Link do TikTok')),
            ],
            options={
                'verbose_name': 'SEO para página comum',
                'verbose_name_plural': 'SEO para páginas comuns',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
