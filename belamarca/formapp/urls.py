from django.urls import path

from . import views

app_name = 'formapp'
urlpatterns = [
    path(
        'contact/',
        views.contact_registration,
        name='contact_registration'
    ),

    path(
        'newsletter/',
        views.newsletter_cadastro,
        name='newsletter_cadastro'
    ),
]
