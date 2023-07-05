import json
import requests
import xmltodict

def consulta_api(input_word):
    
    word = requests.get("https://api.dicionario-aberto.net/word/" + input_word)
    json = word.json()
    try:
      xml = json[0]['xml']
    except:
      return 'OOps, não encontramos essa palavra, verifique se está escrita de forma correta.'
    
    obj = xmltodict.parse(xml)
    input_text = obj['entry']['sense']
    if type(input_text) == list:
      output_text = input_text[0]['def']
    elif type(input_text) == dict:
      output_text = input_text['def']
    if '\n' in output_text:
      output_text = output_text.split('\n')[0]
    if '_' in output_text:
      output_text = output_text.replace('_', '')
      
    return output_text

def validate(slots):

    
    if not slots['PalavraSlot']:
        print("Slot PalavraIntent está vazio")
        return {
        'isValid': False,
        'violatedSlot': 'PalavraIntent'
        }        
        
    
        
    return {'isValid': True}
    
def handle_event_response(event, context):
    
    # print(event)
    slots = event['sessionState']['intent']['slots']
    intent = event['sessionState']['intent']['name']
    print(event['invocationSource'])
    print(slots)
    print(intent)
    
    validation_result = validate(event['sessionState']['intent']['slots'])
    
    if event['invocationSource'] == 'DialogCodeHook':
        if not validation_result['isValid']:
            
            if 'message' in validation_result:
            
                response = {
                "sessionState": {
                    "dialogAction": {
                        'slotToElicit':validation_result['violatedSlot'],
                        "type": "ElicitSlot"
                    },
                    "intent": {
                        'name':intent,
                        'slots': slots
                        
                        }
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": validation_result['message']
                    }
                ]
            } 
            else:
                response = {
                "sessionState": {
                    "dialogAction": {
                        'slotToElicit':validation_result['violatedSlot'],
                        "type": "ElicitSlot"
                    },
                    "intent": {
                        'name':intent,
                        'slots': slots
                        
                        }
                }
            } 
    
            return response
           
        else:
            response = {
            "sessionState": {
                "dialogAction": {
                    "type": "Delegate"
                },
                "intent": {
                    'name':intent,
                    'slots': slots
                    
                    }
            }
        }
            return response
    
    if event['invocationSource'] == 'FulfillmentCodeHook':
        
        input_word = slots['PalavraSlot']['value']['originalValue'].lower()
        significado = consulta_api(input_word)
        
        response = {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                'name':intent,
                'slots': slots,
                'state':'Fulfilled'
                
                }
    
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": significado
            }
        ]
    }
            
        return response