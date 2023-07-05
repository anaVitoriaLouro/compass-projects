import boto3
import os
import json
import requests
from utils.send_sms import send_message

def save_buckets3(media_url, media_type, msg_id):
    save_bucket_s3 = boto3.client('s3')
    
    try:
    # CONDICIONAL PARA ACEITAR O AUDIO ENVIADO
    
        response_audio = requests.head(media_url)
        content_length = response_audio.headers.get('content-length')
        if not content_length:
            sms = send_message("Áudio inválido!",from_number)
            return json.loads(json.dumps(sms, default = str))
            
        content_length = int(content_length)
        print(content_length)
        if content_length > 3000:
            #return "Áudio excede o limite de 3 segundos" # chamar uma função de erro
            sms = send_message("Áudio excede o limite de 3 segundos",from_number)
            return json.loads(json.dumps(sms, default = str))
        
        # DOWNLOAD DO CONTEÚDO DE MÍDIA E SALVAR NO BUCKET S3 PARA TRANSCRIBE
        
        media_save = requests.get(media_url)
        media_content = media_save.content
        media_format = str((media_type.split('/'))[1])
        bucket_name = os.environ['BUCKET_NAME']

        key =(msg_id + '.'+ media_format)
        
        
        save_bucket_s3.put_object(
            Body = media_content,
            Bucket = bucket_name,
            Key = key
        )
        
        media_uri = f's3://{bucket_name}/{key}'
        
        return media_uri
        
    except Exception as e :
        print("Erro ao detectar o texto:", e) # ajustar a função erro
        sms = send_message("Erro no processamento do áudio, favor encaminhar novamente.",from_number)
        return json.loads(json.dumps(sms, default = str))
        
