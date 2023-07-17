from doctest import REPORTING_FLAGS
from mailjet_rest import Client
import os


def send_simple_email(to_email=str, to_name=str, content=dict, attachment=None) -> bool:
    '''
    Exemplo de content (dict) a ser enviado para a função:

    {
    'Subject': 'Título do e-mail',
    'TextPart': 'Texto do e-mail',
    'HTMLPart': 'Conteúdo em HTML do e-mail',
    'CustomID': 'newsletter (exemplo)',
    }

    *Caso você mande um 'HTMLPart', ele irá desconsiderar o TextPart
    no envio do e-mail, ou seja, irá chegar somente o 'HTMLPart' no
    e-mail enviado.

    Caso necessário, você pode mandar um anexo também (attachment),
    o objeto recebido dever conter os atributos content_type, _name, file.
    No caso, a função foi testada com o file sendo um objeto do tipo:
    <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>.
    '''
    api_key = '569b970a6d7157176f840ae31482e219'
    api_secret = '98a9c96ccddb0c660dea589ea20d4bbe'

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')

    from_email = "no-reply@acquamotion.com.br"
    from_name = "Acquamotion - Gramado parks"

    if attachment != None:
        import base64
        content_type = attachment.content_type
        file_name = attachment._name
        file_base_64 = base64.b64encode(attachment.file.getvalue()).decode()

        data = {
            'Messages': [
                {
                    "From": {
                        "Email": from_email,
                        "Name": from_name
                    },
                    "To": [
                        {
                            "Email": to_email,
                            "Name": to_name
                        }
                    ],
                    "Subject": content['Subject'],
                    "TextPart": content['TextPart'],
                    "HTMLPart": content['HTMLPart'],
                    "Attachments": [
                        {
                            "ContentType": content_type,
                            "Filename": file_name,
                            "Base64Content": file_base_64,
                        }
                    ]
                }
            ]
        }
        result = mailjet.send.create(data=data)

        # print(result.status_code)
        # print(result.json())

        if int(result.status_code) == 200:
            return True
        else:
            return False
    else:
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": from_email,
                        "Name": from_name
                    },
                    "To": [
                        {
                            "Email": to_email,
                            "Name": to_name
                        }
                    ],
                    "Subject": content['Subject'],
                    "TextPart": content['TextPart'],
                    "HTMLPart": content['HTMLPart'],
                    "CustomID": content['CustomID'],
                }
            ]
        }
        result = mailjet.send.create(data=data)

        #print (result.status_code)
        #print (result.json())

        if int(result.status_code) == 200:
            return True
        else:
            return False
