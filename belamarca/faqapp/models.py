from django.db import models
from cms.models.pluginmodel import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField


class Disponibility(models.TextChoices):
    DISPONIVEL = 'disponivel', 'Disponível'
    INDISPONIVEL = 'indisponivel', 'Indisponível'

class Ordination(models.TextChoices):
    NEW_TO_OLD = 'new_to_old', 'Dos mais recentes para os mais antigos'
    OLD_TO_NEW = 'old_to_new', 'Dos mais antigos para os mais recentes'
    RANDOM = 'random', 'Ordem aleatória'

#------------------------------------
# 1 - Informações - Perguntas Frequentes
#------------------------------------

class DetailFaqPlugin1(models.Model):

    title = models.CharField(
        max_length=250,
        default='',
        verbose_name='Pergunta',
        help_text='Digite uma pergunta.',
        null=False,
        blank=False,
    )

    description = HTMLField(
        null=False,
        blank=False,
        max_length=4000,
        verbose_name='Resposta',
        help_text='Digite uma resposta para a pergunta.',
        default='',
        configuration='CKEDITOR_SETTINGS',
    )

    disp = models.CharField(
        max_length=12,
        choices=Disponibility.choices,
        default=Disponibility.DISPONIVEL,
        verbose_name='Disponibilidade',
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Pergunta Frequente"
        verbose_name_plural = "Perguntas Frequentes"


class FaqPlugin1(CMSPlugin):

    title = models.CharField(
        max_length=200,
        default='Perguntas Frequentes',
        verbose_name='Título do Perguntas Frequentes',
        help_text='Digite um título para o bloco',
        null=False,
        blank=False,
    )

    ordination = models.CharField(
        max_length=12,
        choices=Ordination.choices,
        default=Ordination.OLD_TO_NEW,
        verbose_name='Ordenação',
    )

    def __str__(self):
        return self.title
