<!--<div>
  <img src="asset\Bot.png" style="box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.3); width: 100px; height: 100px;">
</div> -->
# Avaliação Sprints 9 e 10 - Projeto Final - Programa de Bolsas Compass UOL / AWS e Univesp

Avaliação das sprints 9 e 10 do programa de bolsas Compass UOL para formação em machine learning para AWS.

---

![3imagem](https://github.com/Compass-pb-aws-2023-Univesp/sprint-9-10-pb-aws-univesp/assets/88354075/f24197c4-dbe9-4184-ae7c-ec302ad4b0e6)


# Introdução



Desenvolvimento de um chatbot (ChatBete)  dedicado a auxiliar no reforço da alfabetização de jovens e adultos, especialmente diante dos desafios enfrentados pelo setor da educação no Brasil. Este projeto foi impulsionado pela necessidade de fornecer uma solução que possa ajudar as pessoas a superarem possíveis dificuldades no processo de aprendizado.

A pandemia da COVID-19 trouxe consigo uma série de desafios sem precedentes, afetando significativamente o setor da educação. Com o fechamento das escolas e a transição para o ensino remoto, muitos jovens enfrentaram interrupções em seu processo de alfabetização, uma fase fundamental para o desenvolvimento de habilidades de leitura e escrita. A falta de interação presencial com professores e colegas, além da limitada disponibilidade de recursos educacionais, levou a lacunas no aprendizado e diminuição do engajamento das crianças.




<div align="center" >

![chatbete](https://github.com/Compass-pb-aws-2023-Univesp/sprint-9-10-pb-aws-univesp/assets/117780664/bc77bd73-f559-4357-a6d6-9f58452bb582)

</div>


# Objetivo 

- Com base no contexto apresentado, o projeto visa utilizar o chatbot, como uma ferramenta de inteligência artificial, de forma a auxiliar a preencher essa lacuna e proporcionar um ambiente de aprendizagem virtual interativo e eficaz e promover acesso à educação e combater as consequências negativas da pandemia, garantindo que os jovens tenham a oportunidade de desenvolver habilidades de alfabetização.


# Funcionamento 

# Organização e fluxo de trabalho 
Foi construído um serviço que envolveu:
* Configuração inicial Amazon Lex:
    - Definição das intenções (intents): DitadoIntent, 	RepetirAtividade, SaudacaoIntent e FallbackIntent.
    - Criação dos slots: 
        - AudioSlot para capturar a palavra resposta do rekognition.
        - ReforcarSlot para capturar resposta de continuação ou não da atividade do usuário.
      
* Integração com o Amazon Rekognition:
    - Utilização do Amazon Rekognition para realizar análise de imagens e extrair informações relevantes.

* Integração com o Amazon Polly:
    - Utilização do Amazon Polly para converter texto em voz.

* Integração com o Twilio e WhatsApp:
    - Utilização do serviço do Twilio para enviar mensagens de texto e áudio via WhatsApp.

O chatbot vai interagir com o usuário por meio de mensagens de texto.

* Fluxo de trabalho do chatbot:
    - O chatbot inicia com uma saudação inicial (SaudacaoIntent), fornecendo uma introdução e instruções para o usuário.
    - O usuário será informado sobre a realização de um ditado (DitadoIntent) e receberá um áudio com a palavra.
    - O chatbot solicita ao usuário que envie a foto da palavra ditada, do áudio, via WhatsApp.
    - A foto é recebida pelo Amazon Rekognition e processada utilizando uma função lambda personalizada para conferir se a palavra escrita é a mesma ditada.
    - O chatbot fornece um feedback ao usuário.
    - Após o ditado, o chatbot pode oferecer a opção de realizar outro ditado ou finalizar.

# Arquitetura 

<div align = "center">
<div style="background-color: write;">  
  <img src="asset/arquitetura_final_.GIF">
  <sub>
    <p>Arquitetura do projeto</p><br>
  </sub>
</div>
</div>


## Serviços utilizados

|   Serviço     |     Função |
| ------------- | ------------- |
| [Amazon Lex](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html) | Serviço da AWS para criar interfaces de conversação para aplicativos que usam voz e texto.  |
| [Amazon Recokgnition](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html)   | Facilita a adição de análise de imagem e vídeo aos seus aplicativos.  |
 [Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/what-is.html)   | Serviço de nuvem que converte texto em fala realista.  |
| [Twilio](https://www.twilio.com/pt-br/docs)  | APIs de comunicação para SMS, voz, vídeo e autenticação.  |
[Whatsapp](https://business.whatsapp.com/developers/developer-hub)  |  Aplicativo multiplataforma de mensagens instantâneas e chamadas de voz para smartphones. Além de mensagens de texto, os usuários podem enviar imagens, vídeos e documentos em PDF, além de fazer ligações grátis por meio de uma conexão com a internet.  |
|  [DynamoDB](https://docs.aws.amazon.com/pt_br/step-functions/latest/dg/dynamo-iam.html) | Serviço de banco de dados NoSQL totalmente gerenciado que fornece uma performance rápida e previsível com escalabilidade integrada.  |
|   |  |




# Instalação

## Etapas

- Definição do tema e construção da Arquietura base do projeto;
- Criar chatbot utilizando Amazon Lex;
- Integrar com seguintes serviços da AWS: Rekognition e Polly.
- Criar uma conta no [Twilio](https://www.twilio.com/)
- Integrar com Whatsapp

## Integrando o Amazon Lex com o Whatsapp via Twilio

- Twilio Console -> My account -> Copiar SID e Token

- Amazon Lex Console -> Bot versions -> Deployment -> Channel Integrations -> Add channel -> Platform - Twilio SMS -> Inserir Account SID e Authentication token -> Create -> Copiar url de endpoint gerado

- Twilio Console -> Messaging -> Settings -> Whatsapp sandbox settings -> Colar endpoint copiado em WHEN A MESSAGE COMES IN

# Dificuldades 

Entender todas as integrações que estão na arquitetura do projeto e o desenvolvimento das Lambdas para chamar e receber as informações dos usuários. 

# Referências 

[Kondado](https://kondado.com.br/blog/wiki/2020/11/03/adicionando-o-s3-como-destino-na-plataforma-da-kondado/)

# Desenvolvedores 

[<img src="https://avatars.githubusercontent.com/u/97908745?v=4" width=115><br><sub>Ana Vitória</sub>](https://github.com/anaVitoriaLouro) | [<img src="https://avatars.githubusercontent.com/u/81330043?v=4" width=115><br><sub>Bernardo Lima</sub>](https://github.com/belima93) | [<img src="https://avatars.githubusercontent.com/u/87142990?v=4" width=115><br><sub>Luciene Godoy</sub>](https://github.com/LucieneGodoy) | [<img src="https://avatars.githubusercontent.com/u/72028902?v=4" width=115><br><sub>Luiz Sassi</sub>](https://github.com/luizrsassi) | [<img src="https://avatars.githubusercontent.com/u/88354075?v=4" width=115><br><sub>Kelly Silva</sub>](https://github.com/KellyPLSilva) | [<img src="https://avatars.githubusercontent.com/u/117780664?v=4" width=115><br><sub>Viviane Alves</sub>](https://github.com/Vivianes86)|
| :---: | :---: | :---: | :---: | :---: | :---: | 








