import boto3
import requests
import urllib
import json
import string
from utils.send_sms import send_message

def transcribe_audio(uri_arquivo, media_type,msg_id):
    transcribe_exe = boto3.client('transcribe')
    
    try:
        media_format = str((media_type.split('/'))[1])
        job_name = str(msg_id)
        language_code = 'pt-BR'
        media_uri = uri_arquivo
        
        response = transcribe_exe.start_transcription_job(
            TranscriptionJobName = job_name,
            Media = {'MediaFileUri': media_uri},
            MediaFormat = media_format,
            LanguageCode = language_code
        )
        
        while True:
            response = transcribe_exe.get_transcription_job(TranscriptionJobName = job_name)
            status = response['TranscriptionJob']['TranscriptionJobStatus']

            if status in ['COMPLETED', 'FAILED']:
                break
            
            # Obter a transcrição completa (apenas se estiver concluída)
        if status == 'COMPLETED':
            transcript_uri = urllib.request.urlopen(response['TranscriptionJob']['Transcript']['TranscriptFileUri'])
            data_text = json.loads(transcript_uri.read())
            transcript_text = data_text['results']['transcripts'][0]['transcript']
            
            transcript_text =''.join(filter(lambda x: x not in string.punctuation, transcript_text)) # REMOVE A PONTUAÇÃO, POIS QUANDO TRANSCRITO O AUDIO, E FINALIZA COM PONTO FINAL
                
            
            return transcript_text
            
        else:
            return "Falha na Transcrição!" # Adicionar a função de erro
        
    except Exception as e :
        print("Erro ao detectar o texto:", e)
        return e
        
