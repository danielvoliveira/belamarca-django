from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField


class Disponibility(models.TextChoices):
    DISPONIVEL = 'disponivel', 'Disponível'
    INDISPONIVEL = 'indisponivel', 'Indisponível'

# ------------------------------------------
# 01 - Contato - Formulário para contato com informações de contato
# ------------------------------------------

class FormContactPlugin1(CMSPlugin):

    title = models.CharField(
        verbose_name='Título',
        help_text= 'Título para o formulário.',
        max_length=100,
        default='Fale com a gente :)',
        blank=False,
        null=False,
    )

    subtitle = HTMLField(
        max_length=500,
        verbose_name='Subtítulo',
        help_text= 'Subtítulo para o formulário.',
        configuration='CKEDITOR_SETTINGS',
        default='Preencha o formulário para receber um atendimento exclusivo da nossa equipe.',
        null=False,
        blank=False,
    )

    def __str__(self):
        return str(self.id)


class ContactSubject(models.Model):
    name = models.CharField(
        verbose_name='Nome do assunto',
        max_length=120,
        null=False,
        blank=False,
    )

    responsible_name = models.CharField(
        verbose_name='Nome do responsável pelo assunto',
        max_length=120,
        null=False,
        blank=False,
        default='',
    )

    responsible_email = models.EmailField(
        verbose_name='E-mail do responsável pelo assunto',
        max_length=120,
        null=False,
        blank=False,
        default='',
    )

    disp = models.CharField(
        max_length=12,
        choices=Disponibility.choices,
        default=Disponibility.DISPONIVEL,
        verbose_name='Disponibilidade',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Assunto do formulário de Contato'
        verbose_name_plural = 'Assuntos do formulário de Contato'


class Contact(models.Model):
    name = models.CharField(
        verbose_name='Nome',
        max_length=200,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        verbose_name='E-mail',
        null=False,
        blank=False,
        default='',
    )

    phone = models.CharField(
        verbose_name='Telefone',
        max_length=20,
        default='',
        null=True,
        blank=True,
    )

    subject = models.CharField(
        verbose_name='Assunto',
        max_length=20,
        null=False,
        blank=False,
    )

    message = models.TextField(
        verbose_name='Mensagem',
        max_length=1000,
        default='',
        null=True,
        blank=True,
    )

    terms = models.BooleanField(
        verbose_name='Termos',
        default=False
    )

    def __str__(self):
        return '{} ({})'.format(self.name, self.email)

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"


class FormNewsletterPlugin2(CMSPlugin):

    title = models.CharField(
        verbose_name='Título',
        help_text= 'Título para o formulário.',
        max_length=100,
        default='Cupom de 30% off para você',
        blank=False,
        null=False,
    )

    subtitle = HTMLField(
        max_length=500,
        verbose_name='Subtítulo',
        help_text= 'Subtítulo para o formulário.',
        configuration='CKEDITOR_SETTINGS',
        default='Inscreva-se na nossa newsletter para receber um cumpom de 30% off em seu e-mail.',
        null=False,
        blank=False,
    )

    def __str__(self):
        return str(self.id)

class NewsLetter(models.Model):
    nome = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        max_length=100
    )

    termos = models.BooleanField(
        default=False
    )

    def __str__(self):
        return '{} ({})'.format(self.nome, self.email)

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletter"
