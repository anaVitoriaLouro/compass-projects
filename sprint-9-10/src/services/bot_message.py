import boto3
import os

def bot_response(word):
    lex_client = boto3.client('lexv2-runtime', region_name='us-east-1')
    print('conexao com bot')
    print(word)
    response = lex_client.recognize_text(
        botId=os.environ['BOT_ID'],
        botAliasId= os.environ['BOT_ALIAS_ID'],
        localeId='pt_BR',
        sessionId='1001',
        text=word,
    )
    
    print("resposta do bot", response)
    arr_messages = response['messages']
    bot_response = []
    
    for message in arr_messages:
        bot_response.append(message['content'])
    
    bot_response = "\n".join(bot_response)
    
  
    print(str(bot_response))

    return bot_response
    
