# Avaliação Sprint 4 - Programa de Bolsas Compass UOL / AWS e Univesp

Avaliação da quarta Sprint do Programa de Bolsas Compass-UOL para formação em Machine Learning para AWS.

***

## Grupo 4

[Ana Vitoria Louro Navili ](https://github.com/anaVitoriaLouro)

[Barbara Haydee Presente](https://github.com/Barbarahayd)

[Carlos Roberto de Souza Camilo ](https://github.com/crobertocamilo)

[Kelly Patricia Lopes Silva](https://github.com/KellyPLSilva)

*****
### Objetivo 

Criar uma API em Python com acesso a banco de dados para otimizar o acesso a uma API pública.
******

## Introdução 

*Utilizando o AWS API Gateway*

Disponibilizar uma arquitetura nativa em nuvem orientada a eventos e que permita criar e executar o serviço para rodar sem servidor (*serverless*).

Neste caso, não haverá um servidor online "ouvindo" nossas requisições; quando chega uma requisição, a AWS sobe uma máquina para processá-la e depois a encerra. Isto resulta em economia pois os recursos não ficam ociosos, só ficam online quando houver uma solicitação de serviço. 

O **API Gateway** fornece ferramentas para criar e documentar APIs da Web que roteiam solicitações HTTP para funções do AWS Lambda. 

Isto elimina a necessidade de tarefas de gerenciamento de servidores e transfere as responsabilidades operacionais para AWS, cabendo cliente programar a lógica de sua API através de funções Lambda, inclusive sua integração com banco de dados (também em nuvem). 

<div>

 </div>
 
![funcaoLambda](https://user-images.githubusercontent.com/88354075/229517193-52064606-d7ef-4699-b984-de8bc4490bfc.png)


<div> 

</div>


*O que é o AWS Lambda?*

É um serviço de computação que permite executar código sem o provisonamento ou gerenciamento de servidores. 
O Lambda executa o código em uma infraestrutura de computação de alta disponibilidade e provê toda a administração dos recursos computacionais, incluindo manutenção do servidor e do sistema operacional, provisionamento e escalabilidade automática da capacidade e registro em *logs* do código para praticamente qualquer tipo de aplicação ou serviço de *back-end* (os logs do código podem ser visualizados no **AWS CloudWatch**). 
É necessário fornecer o código em uma das linguagens compatíveis com o Lambda, dentre as quais estão incluídas python e javascript.

*O que é AWS S3?*

É um serviço de armazenamento de objetos que oferece escabilidade, disponibilidade de dados, segurança e performance. Como ele podemos armazenar e proteger qualquer quantidade de dados, aplicações nativas da nuvem e aplicações móveis. No contexto de uma API Gateway, páginas e documentos que serão disponibilizados pela API pode ser armazenados em *buckets* do S3.

*E o banco de dados?*

O **AWS DynamoDB** é um banco de dados NoSQL do tipo chave-valor em nuvem, escalável e com alta disponibilidade e velocidade de gravação. Tabelas no DynamoBD podem ser vinculadas à API, sendo a leitura e gravação de registros de dados (itens) definida no código da função Lambda. 

***
## Descrição 

**Etapas para o desenvolvimento do projeto:**

* O projeto desenvolvido iniciou com o arquivo index.html para disponibilizar a consulta na API. 

* Utilizamos a [API Google Maps - Places](https://developers.google.com/maps/documentation/places/web-service?hl=pt-br) para fazer chamadas de API HTTP. 

* Construção de uma tabela no DynamoBD (localidade, endereço, latitude e longitude).

* Configuração de uma *role* para acesso aos recursos, compreendendo permisões para AWS CloudWatch, API Gateway, Lambda, DynamoDB e S3.
  
Os códigos de uma função no AWS Lambda podem tratar invocações síncronas, no qual a função processa o evento e retorna uma resposta no caso uma localidade. 

* Codificação de uma [função principal do Lambda](https://github.com/Compass-pb-aws-2023-Univesp/sprint-4-pb-aws-univesp/blob/grupo-4/src/lambda_principal.py), responsável por tratar os eventos, tratar as rotas e gerenciar a conexão entre os diversos recursos utilizados. Caso a localidade pesquisada não seja encontrada no banco de dados, é chamada a função [searchLocalidade](https://github.com/Compass-pb-aws-2023-Univesp/sprint-4-pb-aws-univesp/blob/grupo-4/src/external_api.py), responsável por solicitar a pesquisa na API externa (GoogleMaps).

O upload dos arquivos de código é feito diretamente no AWS Lambda, sendo os arquivos em python apresentados na pasta [**src**](https://github.com/Compass-pb-aws-2023-Univesp/sprint-4-pb-aws-univesp/blob/grupo-4/src/) uma cópia destes, adaptada para omitir a chave pessoal utilizada na API externa (o serviço é cobrado quando excedido a franquia gratuita).

* Configuração AWS API Gateway, que coordena as solicitações e as respostas aos clientes.

* Como o desenvolvimento do projeto se deu essencialmente no ambiente da AWS, foram criadas contas de acesso para os membros do grupo, atavés do AWS IAM.

***

## Passos para execução do projeto

Faça o download deste respositório e abra o arquivo [local_index.html](https://github.com/Compass-pb-aws-2023-Univesp/sprint-4-pb-aws-univesp/blob/grupo-4/local_index.html) no navegador. Ao digitar uma localidade no campo de pesquisa e clicar em pesquisar, o API Gateway será acionado e toda a infraestrutura ligada. 

Para fins de testes, foram utilizados parques nacionais e urbanos como localidade. Se a localidade já estiver no banco de dados, o nome da localidade será exibida em maiúsculas; mas se não estiver, será feita uma consulta à API do GoogleMaps e o resultado então apresentado. (Faça um teste, pesquise duas vezes pela mesma localidade; na segunda vez, o nome no resultado será apresentado em maiúsculas, pois terá sido salva no BD na primeira consulta.)

Prototipo versão  1.0
<div>

 </div>


![image (2)](https://user-images.githubusercontent.com/88354075/229509227-265d4429-ffa1-421e-87d8-89617e557eb3.png)

<div> 

</div>


## Passos para reprodução do projeto

Para reproduzir este projeto utilizando os código aqui apresentados, no ambiente da AWS:

1. Faça upload dos códigos para o AWS Lambda, substituindo sua chave pessoal da API do GoogleMaps;
   
2. Configure os demais serviços (DynamoDB, *role* no IAM, API Gateway e S3 - opcional), conforme comentado na **Descrição**. 

3. Após feito o deploy de sua API no Gateway, utilize a URL de execução para acessar os recursos. Por ser uma API *serverless*, os recursos serão carregados apenas quando houver uma requisição, usando apenas os recursos de computação necessários.



### Ferramentas e Tecnologias Utilizadas

*[Visual Studio Code](https://code.visualstudio.com/)

*[AWS: Lambda, API Gateway, CloudWatch, DynamoDB, IAM, S3](https://aws.amazon.com/pt/)

*[Python](https://python.org).

***

### Dificuldades conhecidas:

* Familiaridade com os recursos da AWS e a necessidade de coordenação de diversos serviços para que a API funcione.

* Dificuldade de utilizar o S3 para prover recursos estáticos (página da API e integração entre o *back-end* da função Lambda e o *front-end* HTML armazenado no S3).


*******

Referências:

[Aprofundamento na Categoria - sem servidor](https://aws.amazon.com/pt/getting-started/deep-dive-serverless/)

[CRUD Application Using API Gateway, Lambda, DynamoDB, and Python](https://awstip.com/crud-application-using-api-gateway-lambda-dynamodb-and-python-84d486c87df4)

[Amazon S3](https://aws.amazon.com/pt/s3/)

[Gustavo Pinoti - Desenvolvimento AWS 2020 com foco em Serverless](https://www.udemy.com/course/serverless-aws/)

***






























