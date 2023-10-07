from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from django.views.decorators.cache import cache_page

from .models import (
    GenericPrivacyPolicyPlugin4,
    GenericTermsAndConditionsPlugin5,
)
from validate_email import validate_email
from mainsite.utils.mail_jet_sender import send_simple_email

from .models import (
    NewsLetter,
)

# ------------------------------------------
# 04 - Política e Privacidade - Título e texto
# ------------------------------------------

#@cache_page(60 * 15)
def privacy_policy(request):
    privacy_policy = None
    if GenericPrivacyPolicyPlugin4.objects.filter().exists():
        privacy_policy = GenericPrivacyPolicyPlugin4.objects.filter()
        context = {
            'title': privacy_policy[0].title,
            'text': privacy_policy[0].text,
        }
    else:
        context = {}
    return render(request, "genericapp/generic_privacy_policy_plugin_4.html", context=context)

# ------------------------------------------------------------
# 5 - Termos e Condições - Título subtítulo e texto
# ------------------------------------------------------------

#@cache_page(60 * 15)
def terms_and_conditions(request):
    terms_and_conditions = None
    if GenericTermsAndConditionsPlugin5.objects.filter().exists():
        terms_and_conditions = GenericTermsAndConditionsPlugin5.objects.filter()
        context = {
            'title': terms_and_conditions[0].title,
            'text': terms_and_conditions[0].text,
        }
    else:
        context = {}

    return render(request, "genericapp/generic_terms_and_conditions_5.html", context=context)

# ------------------------------------------
# 06 - Newsletter - Nome, e-mail e termos
# ------------------------------------------

@csrf_exempt
def newsletter_cadastro(request):
    nome = str(request.POST.get('nome', None)).title()
    email = str(request.POST.get('email', None)).lower()
    termos = False

    # Convertendo os termos recebidos para o tipo bool
    if request.POST.get('fcheck', None) == "on":
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

# ------------------------------------------
# 08 - Página 404 - Not found - Título e texto
# ------------------------------------------

def handler404(request, exception):
    return render(request, "genericapp/generic_page_not_found_404.html", context={})
