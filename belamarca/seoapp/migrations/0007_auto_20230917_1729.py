# Generated by Django 3.2.20 on 2023-09-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seoapp', '0006_remove_seometatags_google_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='googleproductmetatag',
            old_name='google_logo',
            new_name='google_product_image',
        ),
        migrations.RemoveField(
            model_name='googlecorporationmetatag',
            name='google_description',
        ),
        migrations.RemoveField(
            model_name='googlecorporationmetatag',
            name='google_name',
        ),
        migrations.RemoveField(
            model_name='googleproductlistmetatag',
            name='google_address_locality',
        ),
        migrations.RemoveField(
            model_name='googleproductlistmetatag',
            name='google_address_region',
        ),
        migrations.RemoveField(
            model_name='googleproductlistmetatag',
            name='google_address_street',
        ),
        migrations.RemoveField(
            model_name='googleproductlistmetatag',
            name='google_address_type',
        ),
        migrations.RemoveField(
            model_name='googleproductlistmetatag',
            name='google_alterantive_name',
        ),
        migrations.RemoveField(
            model_name='googleproductlistmetatag',
            name='google_description',
        ),
        migrations.RemoveField(
            model_name='googleproductlistmetatag',
            name='google_logo',
        ),
        migrations.RemoveField(
            model_name='googleproductlistmetatag',
            name='google_name',
        ),
        migrations.RemoveField(
            model_name='googleproductlistmetatag',
            name='google_social_media_facebook',
        ),
        migrations.RemoveField(
            model_name='googleproductlistmetatag',
            name='google_social_media_instagram',
        ),
        migrations.RemoveField(
            model_name='googleproductlistmetatag',
            name='google_social_media_tiktok',
        ),
        migrations.RemoveField(
            model_name='googleproductlistmetatag',
            name='google_social_media_youtube',
        ),
        migrations.RemoveField(
            model_name='googleproductlistmetatag',
            name='google_telephone',
        ),
        migrations.RemoveField(
            model_name='googleproductmetatag',
            name='google_address_locality',
        ),
        migrations.RemoveField(
            model_name='googleproductmetatag',
            name='google_address_region',
        ),
        migrations.RemoveField(
            model_name='googleproductmetatag',
            name='google_address_street',
        ),
        migrations.RemoveField(
            model_name='googleproductmetatag',
            name='google_address_type',
        ),
        migrations.RemoveField(
            model_name='googleproductmetatag',
            name='google_alterantive_name',
        ),
        migrations.RemoveField(
            model_name='googleproductmetatag',
            name='google_description',
        ),
        migrations.RemoveField(
            model_name='googleproductmetatag',
            name='google_name',
        ),
        migrations.RemoveField(
            model_name='googleproductmetatag',
            name='google_social_media_facebook',
        ),
        migrations.RemoveField(
            model_name='googleproductmetatag',
            name='google_social_media_instagram',
        ),
        migrations.RemoveField(
            model_name='googleproductmetatag',
            name='google_social_media_tiktok',
        ),
        migrations.RemoveField(
            model_name='googleproductmetatag',
            name='google_social_media_youtube',
        ),
        migrations.RemoveField(
            model_name='googleproductmetatag',
            name='google_telephone',
        ),
        migrations.RemoveField(
            model_name='googlewebsitemetatag',
            name='google_address_locality',
        ),
        migrations.RemoveField(
            model_name='googlewebsitemetatag',
            name='google_address_region',
        ),
        migrations.RemoveField(
            model_name='googlewebsitemetatag',
            name='google_address_street',
        ),
        migrations.RemoveField(
            model_name='googlewebsitemetatag',
            name='google_address_type',
        ),
        migrations.RemoveField(
            model_name='googlewebsitemetatag',
            name='google_alterantive_name',
        ),
        migrations.RemoveField(
            model_name='googlewebsitemetatag',
            name='google_description',
        ),
        migrations.RemoveField(
            model_name='googlewebsitemetatag',
            name='google_logo',
        ),
        migrations.RemoveField(
            model_name='googlewebsitemetatag',
            name='google_name',
        ),
        migrations.RemoveField(
            model_name='googlewebsitemetatag',
            name='google_social_media_facebook',
        ),
        migrations.RemoveField(
            model_name='googlewebsitemetatag',
            name='google_social_media_instagram',
        ),
        migrations.RemoveField(
            model_name='googlewebsitemetatag',
            name='google_social_media_tiktok',
        ),
        migrations.RemoveField(
            model_name='googlewebsitemetatag',
            name='google_social_media_youtube',
        ),
        migrations.RemoveField(
            model_name='googlewebsitemetatag',
            name='google_telephone',
        ),
        migrations.RemoveField(
            model_name='seometatags',
            name='social_media_description',
        ),
        migrations.RemoveField(
            model_name='seometatags',
            name='social_media_image',
        ),
        migrations.RemoveField(
            model_name='seometatags',
            name='social_media_site_name',
        ),
        migrations.RemoveField(
            model_name='seometatags',
            name='social_media_title',
        ),
        migrations.AddField(
            model_name='googleproductmetatag',
            name='google_product_code',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Código do Produto'),
        ),
        migrations.AddField(
            model_name='googleproductmetatag',
            name='google_product_description',
            field=models.TextField(blank=True, default='', max_length=300, null=True, verbose_name='Descrição do Produto'),
        ),
        migrations.AddField(
            model_name='googleproductmetatag',
            name='google_product_name',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Nome do Produto'),
        ),
        migrations.AddField(
            model_name='googleproductmetatag',
            name='google_product_price',
            field=models.TextField(blank=True, default='', help_text='Inserir somente o valor no seguinte formato "100.00".', max_length=6, null=True, verbose_name='Preço do Produto'),
        ),
        migrations.AddField(
            model_name='seometatags',
            name='description',
            field=models.TextField(blank=True, default='Bela Marca: para mulheres poderosas como você.', help_text='Dê a cada página uma meta descrição exclusiva que reflita claramente o valor que a página carrega. Inclua suas palavras-chave mais significativas, para que elas possam ser destacadas. Mas tome cuidado para evitar o excesso de palavras-chave, não faça sua descrição apenas uma combinação de palavras-chave que você está segmentando. Limite de 250 caracteres.', max_length=250, null=True, verbose_name='Descrição da página para SEO'),
        ),
        migrations.AddField(
            model_name='seometatags',
            name='image',
            field=models.ImageField(blank=True, default='../../static/assets/seo_default_image/seo_default_image.jpg', help_text='Tamanho ideal 1200x630px.', null=True, upload_to='seo_images/', verbose_name='Imagem para SEO'),
        ),
        migrations.AddField(
            model_name='seometatags',
            name='site_name',
            field=models.CharField(blank=True, default='Bela Marca', max_length=100, null=True, verbose_name='Nome do site para SEO'),
        ),
        migrations.AddField(
            model_name='seometatags',
            name='title',
            field=models.TextField(blank=True, default='Bela Marca: para mulheres poderosas como você.', help_text='Dê a cada página um meta título exclusivo que reflita claramente o valor que a página carrega. Limite de 60 caracteres.', max_length=250, null=True, verbose_name='Título da página para SEO'),
        ),
        migrations.AlterField(
            model_name='googlecorporationmetatag',
            name='google_address_region',
            field=models.CharField(blank=True, default='SP', max_length=2, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='googlecorporationmetatag',
            name='google_type',
            field=models.CharField(choices=[('WebSite', 'Página do Web Site'), ('Organization', 'Organização'), ('ItemList', 'Lista de Produtos'), ('Product', 'Página de Produto')], default='Organization', editable=False, max_length=12, verbose_name='Tipo de página'),
        ),
        migrations.AlterField(
            model_name='googleproductlistmetatag',
            name='google_type',
            field=models.CharField(choices=[('WebSite', 'Página do Web Site'), ('Organization', 'Organização'), ('ItemList', 'Lista de Produtos'), ('Product', 'Página de Produto')], default='ItemList', editable=False, max_length=12, verbose_name='Tipo de página'),
        ),
        migrations.AlterField(
            model_name='googleproductmetatag',
            name='google_type',
            field=models.CharField(choices=[('WebSite', 'Página do Web Site'), ('Organization', 'Organização'), ('ItemList', 'Lista de Produtos'), ('Product', 'Página de Produto')], default='Product', editable=False, max_length=12, verbose_name='Tipo de página'),
        ),
        migrations.AlterField(
            model_name='googlewebsitemetatag',
            name='google_type',
            field=models.CharField(choices=[('WebSite', 'Página do Web Site'), ('Organization', 'Organização'), ('ItemList', 'Lista de Produtos'), ('Product', 'Página de Produto')], default='WebSite', editable=False, max_length=12, verbose_name='Tipo de página'),
        ),
        migrations.AlterField(
            model_name='seometatags',
            name='social_media_type',
            field=models.CharField(choices=[('organization', 'Organização/Empresa'), ('website', 'Página Web'), ('blog', 'Página principal do blog')], default='website', editable=False, max_length=12, verbose_name='Tipo de página para Instagram e Facebook'),
        ),
        migrations.AlterField(
            model_name='seosinglepageplugin1',
            name='google_type',
            field=models.CharField(choices=[('WebSite', 'Página do Web Site'), ('Organization', 'Organização'), ('ItemList', 'Lista de Produtos'), ('Product', 'Página de Produto')], default='Organization', editable=False, max_length=12, verbose_name='Tipo de página'),
        ),
    ]