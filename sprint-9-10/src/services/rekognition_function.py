from io import BytesIO
import requests
import boto3
import string
import json 
from botocore.exceptions import NoCredentialsError
from utils.send_sms import send_message



def rekognition_det_text(media_url,from_number):
    rekognition_exe = boto3.client('rekognition')
    
    try:
        response_image = requests.get(media_url)
        image_data = response_image.content
    
        response = rekognition_exe.detect_text(
            Image = {
                'Bytes':image_data
                }
        )
        textDetections = response['TextDetections']
    
        list_word = []
        for text in textDetections:
            Detected_text = text['DetectedText']
            list_word.insert(-1,Detected_text)
            list_word = sorted(set(list_word))
            list_word = max(list_word, key=len)
    
            return list_word

    except Exception as e :
        print("Erro ao detectar o texto:", e)
        return e
