import json
import urllib.parse
from utils.send_sms import send_message
from utils.s3_transcribe_save import save_buckets3
from services.transcribe_function import transcribe_audio
from services.rekognition_function import rekognition_det_text
from services.bot_message import bot_response


def lambda_handler(event, context):

    from_number = urllib.parse.unquote(event['From'])
    msg_id = event['SmsMessageSid'] # ID SMS TWILIO
   

    
    try:
        if 'MediaUrl0' in event:
            media_url = urllib.parse.unquote(event['MediaUrl0']) # URL TWILIO DO ARQUIVO DE MIDIA
            media_type = urllib.parse.unquote(event['MediaContentType0']) # TIPO DE ARQUIVO
            #msg_id = event['SmsMessageSid'] # ID SMS TWILIO
            
            if media_type.startswith('audio/'):
                uri_arquivo = save_buckets3(media_url,media_type,msg_id,from_number)
                word = transcribe_audio(uri_arquivo,media_type,msg_id,from_number)


                bot_result = bot_response(word)
                
            elif media_type.startswith('image/'):
                word = rekognition_det_text(media_url,from_number)
                bot_result = bot_response(word)
                

        else:
            word = urllib.parse.unquote(event['Body'])
            bot_result = bot_response(word)

            
            
    # MENSAGEM DE RETORNO PARA USUARIO
    
        sms = send_message(bot_result, from_number)
        return json.loads(json.dumps(sms, default = str))
            
    except Exception as e:
        print('Erro ao detectar a mensagem, encaminhe novamente',e)
        sms = send_message('Erro ao detectar a mensagem, encaminhe novamente',from_number)
        return json.loads(json.dumps(sms, default = str))
