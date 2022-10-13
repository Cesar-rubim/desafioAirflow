# Desafio Airflow - Indicium

Este repositório é dedicado a um simples projeto apenas para demonstrar competências básicas na ferramenta de orquestração de tarefas Airflow.

## Descrição do projeto
O projeto consiste em três tarefas (tasks) simples:

1. Ler a tabela Order do banco de dados Northwind_small.sqlite, localizado em dags/desafioAirflow/data e salvar os dados no arquivo output.csv, localizado em dags/desafioAirflow/data;

2. Ler  a tabela OrderDetails do banco Northwind_small.sqlite, realizar um join dos dados do csv do item anterior com a a tabela obtida e em seguida, calcular a quantidade vendida com destino para a cidade de Rio de Janeiro, exportanto o resultado para o arquivo count.txt, também localizado em dags/desafioAirflow/data;

3. Enviar um e-mail com o resultado do item anterior, utilizando o conceito de Variáveis internas do Airflow.

## Utilização do projeto

No intuito de exercitar o domínio do processo de conteinerização, foi utilizada a ferramenta Docker, sendo assim necessário instalar o Docker e o Docker Compose. Pressupondo que o Docker esteja instalado corretamente, preparemos o ambiente criando um ambiente virtual do python dentro da pasta inicial do projeto. No terminal (já dentro da pasta do projeto)

```
python3 -m venv venv
source venv/bin/activate
```

Para rodar o container de docker, ainda na pasta em questão

```
docker-compose up
```

Pronto! O Airflow poderá ser acessado pelo navegador em localhost:8080, com a task desafioAirflow pronta para ser executada.


