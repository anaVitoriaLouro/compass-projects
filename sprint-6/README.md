# Avaliação Sprint 6 - Programa de Bolsas Compass UOL / AWS e Univesp

Avaliação da [sexta sprint][sprint6main] do programa de bolsas [Compass UOL][compass] para formação em machine learning para [AWS][aws].
***

# Sistema de indexação de mensagens de áudio com AWS

Este é um sistema de indexação de mensagens de áudio, que utiliza ferramentas AWS, como Amazon Transcribe, Amazon Comprehend e Elasticsearch. O objetivo do sistema é permitir a indexação de mensagens de áudio em um banco de dados.


***
## Funcionamento
O sistema funciona da seguinte forma:

1. O usuário faz upload de um arquivo de áudio existente.
2. O áudio é enviado para o Amazon S3 para armazenamento.
3. O Amazon Transcribe é utilizado para transcrever o áudio em texto.
4. O texto transcrito é enviado para o Amazon Comprehend, que analisa o texto e extrai informações relevantes.
5. Os dados extraídos do texto são indexados no Elasticsearch.
6. O usuário pode realizar uma pesquisa no sistema para encontrar mensagens de áudio relevantes com base em palavras-chave.

# Pré-requisitos e limitações
- Antes de iniciar a configuração do sistema, é necessário ter uma conta AWS ativa e configurada.
- Certifique-se de que o arquivo esteja no formato FLAC, MP3, MP4, Ogg, Webm, AMR ou WAV.
- O arquivo de deve ter menos de 4 horas de duração e menos de 2 gb de tamanho.

## Ambiente
O projeto foi desenvolvido utilizando o ambiente AWS. Os seguintes serviços da AWS foram usados:
- IAM Role 
- Amazon S3: Armazenamento de dados
- Amazon Transcribe: Serviço de reconhecimento de fala para converter áudio em texto;
- Amazon Comprehend: Serviço de análise de texto para extrair informações relevantes, tais como entidades e sentimentos;
- AWS Lambda: Serviço de computação sem servidor que permite executar códigos sem gerenciar servidores;
- AWS Step Functions: Serviço para coordenação de aplicações sem servidor que permite construir e executar workflows;
- Amazon Elasticsearch Service: Serviço gerenciado de Elasticsearch, um motor de busca e análise distribuído;
- Amazon Cognito: Serviço de autenticação e autorização para aplicações web e mobile.

## Como Executar o Projeto
- Clone o repositório do projeto para o seu computador.
- Siga o tutorial apresentado em https://aws.amazon.com/pt/blogs/aws-brasil/indexando-audios-com-amazon-transcribe-amazon-comprehend-e-elasticsearch/ para configurar as ferramentas AWS e realizar o deploy da aplicação. Certifique-se de adaptar e atualizar o código conforme necessário.
- Crie uma interface online ou encaminhe um áudio, como apresentado em https://aws.amazon.com/pt/blogs/compute/uploading-to-amazon-s3-directly-from-a-web-or-mobile-application/. A interface deve permitir que o usuário grave ou faça upload de um arquivo de áudio e envie-o para o Amazon S3.
- Configure o Elasticsearch para permitir a indexação dos dados extraídos do texto transcrito pelo Amazon Transcribe e analisados pelo Amazon Comprehend. Certifique-se de criar um índice adequado e mapear os campos relevantes.
- Acessar o bucket de saída e realizar o download do arquivo JSON com a transcrição.

## Interface para upload do áudio
O Front-end desenvolvido neste projeto para o carregamento do arquivo de áudio pode ser acessado clicando [aqui][front] ou acesse o endereço abaixo na barra de endereço do seu navegador de preferência.
```sh
http://projeto-sprint-06-raws3bucket-1x832a5h6k9q2.s3-website-us-east-1.amazonaws.com/
```

## Arquivos do Projeto
- README.md: Este arquivo README.
- ThreelittlePigs-example_pt-BR.mp3: Arquivo de áudio utilizado para teste, gearado através de https://freetts.com/Home/PortugueseTTS
- transcribe-ThreelittlePigs-example.json: Arquivo JSON com as transcrições obtidas apartir do áudio enviado (ThreelittlePigs-example_pt-BR.mp3).

## Conclusão
Este sistema de indexação de mensagens de áudio com ferramentas AWS pode ser útil para empresas e organizações que precisam gerenciar grandes quantidades de dados de áudio e facilitar o acesso a informações relevantes. É importante lembrar que a configuração e utilização do sistema requerem conhecimentos em programação e AWS.

## Referências
- Indexando áudios com Amazon Transcribe, Amazon Comprehend e ElasticSearch.
https://aws.amazon.com/pt/blogs/aws-brasil/indexando-audios-com-amazon-transcribe-amazon-comprehend-e-elasticsearch/
- Uploading para o Amazon S3 diretamente de um aplicativo web ou móvel.
https://aws.amazon.com/pt/blogs/compute/uploading-to-amazon-s3-directly-from-a-web-or-mobile-application/
- Gerador de audio apartir de texto.
https://freetts.com/Home/PortugueseTTS

## Dificuldades
Durante o desenvolvimento do projeto, uma das principais dificuldades encontradas foi a configuração adequada do ambiente. Para utilizar as ferramentas AWS, foi necessário criar e configurar corretamente as credenciais e as permissões de acesso.


***


## Desenvolvedores do projeto
| [<img src="https://avatars.githubusercontent.com/u/97908745?v=4" width=115><br><sub>Ana Vitória Louro Navili</sub>](https://github.com/anaVitoriaLouro)|  [<img src="https://avatars.githubusercontent.com/u/112827096?v=4" width=115><br><sub>Barbara Haydee Presente</sub>](https://github.com/Barbarahayd) |[<img src="https://avatars.githubusercontent.com/u/25699466?v=4" width=115><br><sub>Bruno Monserrat Perillo</sub>](https://github.com/brunoperillo) | [<img src="https://avatars.githubusercontent.com/u/87142990?v=4" width=115><br><sub>Luciene Godoy</sub>](https://github.com/LucieneGodoy) | [<img src="https://avatars.githubusercontent.com/u/72028902?v=4" width=115><br><sub>Luiz Renato Sassi</sub>](https://github.com/luizrsassi) |
| :---: | :---: | :---: |:---: |:---: |


***
   [kernel]: <https://pt.wikipedia.org/wiki/N%C3%BAcleo_(sistema_operacional)>
   [compass]: <https://compass.uol/en/home/>
   [aws]: <https://aws.amazon.com/pt/>
   [sprint6main]: <https://github.com/Compass-pb-aws-2023-Univesp/sprint-6-pb-aws-univesp/tree/main>
   [front]: <http://projeto-sprint-06-raws3bucket-1x832a5h6k9q2.s3-website-us-east-1.amazonaws.com/>
