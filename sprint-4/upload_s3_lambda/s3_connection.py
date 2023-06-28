# da pra usar a bilbioteca boto3 do python p/ acessar os arquivos no bucket S3
import boto3

s3 = boto3.client('s3')

'''Esse código acessa os arquivos index.html e style.css no bucket S3 e os armazena nas 
variáveis html_body e css_body'''

def handler(event, context):
    html_object = s3.get_object(Bucket='<nome do bucket>', Key='index.html')
    css_object = s3.get_object(Bucket='<nome do bucket>', Key='style.css')

    html_body = html_object['Body'].read().decode('utf-8')
    css_body = css_object['Body'].read().decode('utf-8')


# aqui pode processar os arquivos HTML e CSS como quiser
