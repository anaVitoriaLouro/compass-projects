import urllib.request, urllib.parse, urllib.error
import http
import json
import time
import ssl
import sys
import codecs

def searchPlace(localidade):
    """
    Pesquisa o endereço e as coordenadas de uma localidade usando uma API externa.

    Args:
    localidade: o nome ou endereço da localidade a ser pesquisada

    Returns:
    - Uma tupla com o endereço, latitude e longitude da localidade pesquisada, ou None se a pesquisa falhar.
    """

    #Chave da API
    api_key = #Cole sua chave da API aqui

    # Ignora erros de certificado SSL
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    address = localidade.strip()

    #Pesquisa a localidade na API externa
    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print(f'Pesquisando por "{localidade}" na API...')
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print(f'Concluído. Recebidos {len(data)} caracteres da API.')
    print('Analisando resultado...')

    #Tentativa de decodificar o objeto JSON recebido da API externa
    try:
        js = json.loads(data)
    except:
        print('Possível falha na codificação do resultado (unicode error):')
        print(data)
        return None

    #Verifica se a pesquisa na API retornou um resultado válido
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Falha ao analisar o resultado. Por favor, tente novamente. ====')
        print(data)
        return None

    else:

        #Análise do objeto JSON válido recebido como resposta
        try: 
            js = json.loads(str(data))

            latitude = js["results"][0]["geometry"]["location"]["lat"]
            longitude = js["results"][0]["geometry"]["location"]["lng"]
            endereco = js['results'][0]['formatted_address']
            endereco = endereco.replace("'", "")

            print('\nResultado:')
            print(f'Localidade: {localidade}')
            print(f'Endereço: {endereco}')
            print(f'Coordenadas: {latitude},{longitude}\n')
        
            return (endereco,latitude,longitude)
        
        except:
            print('Local não pode ser identificado.\n')
            return None
            