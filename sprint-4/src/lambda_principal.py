import boto3
import json
from external_api import searchPlace
from decimal import Decimal
import logging 
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Associa a tabela 'Locais' do DynamoDB
dynamodbTableName = 'Locais'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodbTableName)

s3 = boto3.client('s3')


getMethod = 'GET'
postMethod = 'POST'
statusPath = '/status'
testPath = '/test'
rootPath = '/'


def lambda_handler(event, contest):
    """
    Função principal que é acionada pelo AWS Lambda.
    
    Args:
    - event: dict contendo as informações sobre a requisição HTTP recebida.
    - context: objeto do tipo LambdaContext que fornece informações sobre o ambiente de execução.
    
    Returns:
    - response: dict contendo o status code HTTP, os headers da resposta e o body.
    """
    
    logger.info(event)
    httpMethod = event['httpMethod']
    path = event['path']

    if httpMethod == getMethod and path == statusPath:
         response = buildResponse(200, 'A API está online')
    elif httpMethod == getMethod and path == rootPath:
        #response = buildResponse(200, 'Você está na raiz.')
        response = getLocalidade(event['queryStringParameters']['localidade'])
    elif httpMethod == getMethod and path == testPath:
        #response = buildResponse(200, 'Rota para testes.')
        
        # Recupera o objeto do S3
        s3_response = s3.get_object(Bucket='sprint3-arquivos', Key='index.html')
        html_content = s3_response['Body'].read().decode('utf-8')

        # Constrói a resposta HTTP
        response = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',
                'Access-Control-Allow-Origin': '*'
            },
            'body': html_content
        }
    
    elif httpMethod == postMethod and path == testPath:
        print('Teste post')
        
    else:
        response = buildResponse(404, 'Página não encontrada.')

    return response


def getLocalidade(localidade):
    """
    Busca a localidade na tabela do DynamoDB. Se não encontrada, faz uma pesquisa na API externa e salva o resultado na tabela.

    Args:
    - localidade: string contendo o nome da localidade a ser buscada.

    Returns:
    - response: dict contendo o status code HTTP, os headers da resposta e o body.
    """

    try:
        #Pesquisa a localidade na tabela da banco de dados
        response = table.get_item(
            Key={
                'localidade': localidade.upper()
            }
        )
        
        #Se for encontrado no BD, retorna o registro salvo
        if 'Item' in response:
            
            Item = response['Item']
            Item['latitude'] = float(Item['latitude'])
            Item['longitude'] = float(Item['longitude'])
            
            print('Registro encontrado no banco de dados.')
            return buildResponse(200, Item)
        
        else:
            
            #Se não registro no BD, solicita uma pesquisa na API externa
            novo_local = searchPlace(localidade)
            
            if novo_local == None:
                return buildResponse(404, {'Message': 'Localidade NÃO ENCONTRADA. Especifique melhor a sua pesquisa e tente novamente.'})
            
            else:
                novo_Item = {
                    "localidade": localidade,
                    "endereco": novo_local[0],
                    "latitude": novo_local[1],
                    "longitude": novo_local[2]
                }
    
                print(novo_Item)

                #Formata o novo item no padrão exigido e salva na tabela
                formatted_new_Item = {
                    "localidade": localidade.upper(),
                    "endereco": novo_local[0],
                    "latitude": Decimal(str(novo_local[1])),
                    "longitude": Decimal(str(novo_local[2]))
                }

                table.put_item(Item = formatted_new_Item)
                
                return buildResponse(200, novo_Item)
                
    except:
        logger.exception('Log it here for now')



def buildResponse(statusCode, body=None):
    """
    Constrói um dicionário contendo informações sobre a resposta HTTP que será enviada.

    Args:
    - statusCode: int indicando o código de status HTTP da resposta.
    - body: opcional. Objeto que será serializado para JSON e adicionado ao corpo da resposta.

    Returns:
    - response: dict contendo o status code HTTP, os headers da resposta e o body (se fornecido).
    """
    
    response = {
        'statusCode': statusCode,
        'headers': {
            'ContentType': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    if body is not None:
        response['body'] = json.dumps(body, ensure_ascii=False)

    return response