from django.shortcuts import render
from django.http import JsonResponse
from mainsite.utils.mail_jet_sender import send_simple_email
from validate_email import validate_email
import requests
from .models import (
    Contact,
    ContactSubject,
    NewsLetter,
)


# ------------------------------------------
# 01 - Contato - Formulário para contato com informações de contato
# ------------------------------------------

def contact_registration(request):
    name = str(request.POST.get('name', None)).title()
    email = str(request.POST.get('email', None))
    phone = str(request.POST.get('phone', None))
    subject = request.POST.get('subject', None)
    message = str(request.POST.get('message', None)).capitalize()
    terms = False

    if request.POST.get('contact-check', None) == "on":
        terms = True

    if(name == "" and email == "" and str(subject) == "None" and message == ""):
        context = {
            'status': 0,
            'message': 'Os campos com asterisco são de preenchimento obrigatório.'
        }
        return JsonResponse(context)
    if name == "" or len(name) < 3:
        context = {
            'status': 0,
            'message': 'O nome informado deve conter no mínimo 3 caracteres.'
        }
        return JsonResponse(context)

    if validate_email(email) == False:
        context = {
            'status': 0,
            'message': 'Informe um endereço de e-mail válido.'
        }
        return JsonResponse(context)

    if phone != "None":
        to_remove = "$(#.-*"
        for caracter in to_remove:
            phone = phone.replace(caracter, '')

        try:
            int(phone)
        except ValueError:
            context = {
                'status': 0,
                'message': 'Insira um numero de telefone válido.'
            }
            return JsonResponse(context)
    else:
        phone = ""

    if subject == None:
        context = {
            'status': 0,
            'message': 'Você deve selecionar um assunto.'
        }
        return JsonResponse(context)

    if len(message) < 20:
        context = {
            'status': 0,
            'message': 'A mensagem deve conter no mínimo 20 caracteres.'
        }
        return JsonResponse(context)

    if terms == False:
        context = {
            'status': 0,
            'message': 'É preciso concordar com nossos termos para realizar o envio.'
        }
        return JsonResponse(context)

    # Cadastrando dados após validação dos detalhes
    new_contact = Contact(
        name=name,
        email=email,
        phone=phone,
        subject=subject,
        message=message,
        terms=terms,
    )
    new_contact.save()

    # Lendo a página HTML do template de e-mail

    # url = "http://s3.amazonaws.com/mailmkt.lo/gramado_parks/Acquamotion_boasvindas_2_v4/Acquamotion_boasvindas_2_v4.html"

    # template_email = requests.get(url)

    #content = {
    #    'Subject': 'Contato enviado com sucesso.',
    #    'TextPart': '',
    #    'HTMLPart': '<p>Olá, tudo bem? <br><br>{name} acabou de se cadastrar no formulário de contato.</p><br><h3>Dados cadastrados:</h3><p>Nome: {name} <br><br> E-mail: {email} <br><br> Telefone: {phone} <br><br> Assunto: {subject} <br><br> Mensagem: {message} <br><br><br> Att., <br>Acquamotion Site. </p>'.format(name=name, email=email, phone=phone, subject=subject, message=message),
    #    'CustomID': 'TrabalheConosco',
    #}

    # Pegando o e-mail responsável pela área
    #current_subject = ContactSubject.objects.filter(name=subject)
    #responsible_name = current_subject[0].responsible_name
    #responsible_email = current_subject[0].responsible_email

    #send_to = [str(responsible_email), str(responsible_name)]

    #if send_simple_email(responsible_email, responsible_name, content) == True:
    context = {
        'status': 1,
        'message': 'Contato enviado com sucesso.'
    }
    return JsonResponse(context)

def newsletter_cadastro(request):
    nome = str(request.POST.get('nome', None)).title()
    email = str(request.POST.get('email', None)).lower()
    termos = False

    # Convertendo os termos recebidos para o tipo bool
    if request.POST.get('news-check', None) == "on":
        termos = True

    # Verificando se nome e e-mail foram preenchidos.
    if nome == "" or len(nome) < 3 or email == "":
        if nome == "" and email == "" and termos:
            context = {
                'status': 0,
                'message': 'Você deve informar seu nome, e-mail e concordar com nossos termos.'
            }
        # Verificando se nome foi preenchido e tem mais de 3 caracteres
        elif nome == "" or len(nome) < 3:
            context = {
                'status': 0,
                'message': 'O nome informado deve conter no mínimo 3 caracteres.'
            }
        # Verificando se e-mail foi preenchido
        elif email == "":
            context = {
                'status': 0,
                'message': 'Você deve informar o seu endereço de e-mail.'
            }
        else:
            pass
        return JsonResponse(context)

    if validate_email(email) == False:
        context = {
            'status': 0,
            'message': 'Informe um endereço de e-mail válido.'
        }
        return JsonResponse(context)

    # Verificando a concordância com os termos
    if termos == False:
        context = {
            'status': 0,
            'message': 'É preciso concordar com nossos termos para realizar o cadastro.'
        }
        return JsonResponse(context)

    # Verificando se o e-mail já foi cadastrado.
    verific_email = NewsLetter.objects.filter(email=email)
    if len(verific_email) > 0:
        context = {
            'status': 0,
            'message': 'O e-mail informado já está cadastrado em nosso sistema.'
        }
        return JsonResponse(context)

    # Lendo a página HTML do template de e-mail

    # url = "http://s3.amazonaws.com/mailmkt.lo/gramado_parks/Acquamotion_boasvindas_2_v4/Acquamotion_boasvindas_2_v4.html"

    # template_email = requests.get(url)

    # Cadastrando dados após validação dos detalhes
    nova_newsletter = NewsLetter(nome=nome, email=email, termos=termos)
    nova_newsletter.save()
    #content = {
    #    'Subject': 'Novo cadastro de Newsletter em Acquamotion',
    #    'TextPart': '',
    #    'HTMLPart': '<p>Olá!<br><br>{nome} acabou de se cadastrar para receber as newsletters.</p><h3>Dados cadastrados:</h3><p>Nome: {nome} <br> E-mail: {email} <br><br> Att., <br>Acquamotion. </p>'.format(nome=nome, email=email),
    #    'CustomID': 'Newsletter',
    #}

    #send_to = {
    #    'first': ['rosania.silva@gramadoparks.com', 'Rosania Silva'],
    #}

    #send_simple_email(send_to['first'][0], send_to['first'][1], content)

    context = {
        'status': 1,
        'message': 'Cadastro realizado com sucesso.'
    }
    return JsonResponse(context)