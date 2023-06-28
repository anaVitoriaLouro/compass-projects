# Avaliação Sprint 5 - Programa de Bolsas Compass UOL / AWS e Univesp

Avaliação da quinta sprint do programa de bolsas Compass UOL para formação em machine learning para AWS.

***

## Grupo-2

- [Ana Vitória Louro](https://github.com/anaVitoriaLouro)
- [Bernardo Lima](https://github.com/belima93)
- [Diego Lopes](https://github.com/Diegox0301)
- [Luciene Godoy](https://github.com/LucieneGodoy)

***

# Rock Paper Scissors AI - Reconhecimento de imagens

## Objetivo

Execução de treinamento de dataset [rock_paper_scissor](https://www.tensorflow.org/datasets/catalog/rock_paper_scissors?hl=pt-br) para posterior reconhecimento.

<div align="center">

![rock-paper-scissor](https://user-images.githubusercontent.com/81330043/232077729-91c7d1e3-5403-48e9-a713-e1dcf7cca685.png)

</div>


### Descrição

Este projeto consiste em um modelo de aprendizado de máquina treinado para reconhecer o movimento em um jogo de pedra-papel-tesoura com base na posição da mão. 

O conjunto de dados para treinamento e teste foram gerados por IA para garantir a precisão e a qualidade do modelo. O modelo foi desenvolvido usando uma arquitetura de rede neural profunda CNN (Convolutional Neural Network).

Para treinar o modelo, foi utilizada a plataforma AWS Sagemaker, que fornece um ambiente escalável e fácil de usar para treinar e implantar modelos de machine learning. Além disso, o modelo treinado e o dataset de inferência foram armazenados em bucket S3 da AWS.

***

### Execução do Projeto

- Instalações e importações de bibliotecas para o desenvolvimento;
- Análise exploratória do Dataset em busca de informações relevantes;
- Preparação dos dados para treinamento do modelo; 
- Iniciando o treinamento utilizando Keras;
- Aplicando técnica de Hyperparameter Tuning buscando acurácia maior;
- Modelo obteve acurácia de:
    - Aplicando Hypermarameter Tuning - 79%
- Criação e Armazenamento do modelo em Bucket S3 na AWS;
    - O Amazon S3 (Simple Storage Service) é um serviço de armazenamento de objetos da Amazon Web Services (AWS) que fornece escalabilidade, disponibilidade de dados, segurança e desempenho para armazenamento e recuperação de dados na nuvem.

- Link para o Bucket e DataSet estão disponiveis dentro do notebook


***

### Ferramentas e Tecnologias Utilizadas

- [Amazon SageMaker e S3](https://aws.amazon.com/pt/)
- [Tensorflow: datasets e Keras](https://www.tensorflow.org/?hl=pt-br)
- [Amazon SageMaker Studio Lab](https://studiolab.sagemaker.aws/)
- [Google Colab](https://colab.research.google.com/)
- [Python: NumPy, Matplotlib](https://python.org).

***

### Dificuldades Registradas

- Familiaridade com novas ferramentas como: SageMaker e Tensorflow;
