from django.urls import path
from . import views

app_name = 'genericapp'

urlpatterns = [
    path(
        'politicas-de-privacidade/',
        views.privacy_policy,
        name='privacy_policy'
    ),
    path(
        'termos-e-condicoes/',
        views.terms_and_conditions,
        name='terms_and_conditions'
    ),
    path(
        'cadastro-newsletter-e-promocoes/',
        views.newsletter_cadastro,
        name='newsletter_cadastro'
    ),
    path(
        'reagenadamento-cancelamento-e-no-show/',
        views.schedule_and_noshow,
        name='schedule_and_noshow'
    )
]
