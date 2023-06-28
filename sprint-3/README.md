# Avaliação Sprint 3 - Programa de Bolsas Compass UOL / AWS e Univesp

Avaliação da segunda sprint do programa de bolsas [Compass UOL][compass] para formação em machine learning para [AWS][aws].

***

## Objetivo
Este projeto é uma aplicação web, com implementação [docker][dockerwiki] para ser executada na nuvem da [AWS Cloud][aws]. O objetivo desta dockerização é facilitar o processo de implantação da aplicação em um ambiente escalável e replicável.

## Introdução
[Docker][dockerwiki] é um conjunto de produtos de [plataforma como serviço (PaaS)][pass] que usam [virtualização de nível de sistema operacional][virtualizacao] para entregar software em pacotes chamados contêineres. Os contêineres são isolados uns dos outros e agrupam seus próprios softwares, bibliotecas e arquivos de configuração. Eles podem se comunicar uns com os outros por meio de canais bem definidos. Todos os contêineres são executados por um único [kernel do sistema operacional][kernel] e, portanto, usam menos recursos do que as [máquinas virtuais][vm].

A [Sprint 03][sprint3main] foi desenvolvida para implementar um contêiner docker a partir do projeto da [Sprint 02][sprint2main].

## Aplicação da execução do projeto
A descrição de toda implementação pode ser consultado [aqui][tutorial].

A síntese da [Sprint 03][sprint3main] é descrita como:
- Trazer o HTML do [projeto anterior][sprint1] e criar o arquivo js para carregar o index.htmL.
- Gerar uma imagem dentro do VS code 
- Enviar o conteiner para infraestrutura da AWS.

## Técnicas e tecnologias utilizadas
- Visual Studio
- HTML5
- Node.js
- JavaScript
- Docker
- AWS

## Instrução de uso
Verifique o deploy deste projeto clicando [aqui][pagina] ou acesse o endereço abaixo na barra de endereço do seu navegador de preferência.
```sh
54.163.32.88:9000
```


## Dificuldades
- Familiariedade no uso do Docker, AWS e Node.js.
- Documentação do desenvolvimento do projeto.

***

## Desenvolvedores do projeto
| [<img src="https://avatars.githubusercontent.com/u/97908745?v=4" width=115><br><sub>Ana Vitória Louro Navili</sub>](https://github.com/anaVitoriaLouro) | [<img src="https://avatars.githubusercontent.com/u/25699466?v=4" width=115><br><sub>Bruno Monserrat Perillo</sub>](https://github.com/brunoperillo) | [<img src="https://avatars.githubusercontent.com/u/96358027?v=4" width=115><br><sub>Diego Lopes da Silva</sub>](https://github.com/Diegox0301) | [<img src="https://avatars.githubusercontent.com/u/88354075?v=4" width=115><br><sub>Kelly Patricia Lopes Silva</sub>](https://github.com/KellyPLSilva) |
| :---: | :---: | :---: |:---: |


***
   [projeto]: <https://github.com/Compass-pb-aws-2023-Univesp/sprint-2-pb-aws-univesp.git>
   [dockerwiki]: <https://pt.wikipedia.org/wiki/Docker_(software)>
   [pass]: <https://pt.wikipedia.org/wiki/Plataforma_como_servi%C3%A7o>
   [virtualizacao]: <https://pt.wikipedia.org/wiki/Virtualiza%C3%A7%C3%A3o_em_n%C3%ADvel_de_sistema_operacional>
   [kernel]: <https://pt.wikipedia.org/wiki/N%C3%BAcleo_(sistema_operacional)>
   [tutorial]: <https://github.com/Compass-pb-aws-2023-Univesp/sprint-3-pb-aws-univesp/blob/grupo-4/files/descricao.pdf>
   [vm]: <https://pt.wikipedia.org/wiki/M%C3%A1quina_virtual>
   [cloud]: <https://pt.wikipedia.org/wiki/Computa%C3%A7%C3%A3o_em_nuvem>
   [compass]: <https://compass.uol/en/home/>
   [aws]: <https://aws.amazon.com/pt/>
   [sprint1]: <https://github.com/Compass-pb-aws-2023-Univesp/sprint-1-pb-aws-univesp>
   [sprint2main]: <https://github.com/Compass-pb-aws-2023-Univesp/sprint-2-pb-aws-univesp>
   [sprint3main]: <https://github.com/Compass-pb-aws-2023-Univesp/sprint-3-pb-aws-univesp>
   [notion]: <https://ludicrous-help-e3a.notion.site/Sprint-2-f7fe80d6068b41ffbded94a3a28e32a9>
   [pagina]: <http://54.163.32.88:9000/>
