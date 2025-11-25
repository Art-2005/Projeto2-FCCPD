# Projeto2-FCCPD

# Desafio 1 

Este desafio consiste em criar dois containers Docker que se comunicam através de uma rede customizada.  
A solução utiliza um **servidor Flask** e um **cliente curl** para demonstrar a comunicação contínua entre os serviços.

## Arquitetura

A solução é composta por dois containers feitos nas pastas:

### **1. Servidor (Flask)**

`app.py`: Executa a aplicação Flask na porta **8080** e responde requisições HTTP GET

`Dockerfile`: Constroi a imagem localmente, instala as requisições do requirements.txt e por no fim copia o codigo e executa o comando `python app.py`

### **2. Cliente (curl)**

`Dockerfile`: Executa um loop infinito chamando `http://server:8080` a cada 5 segundos e mostra no terminal as respostas recebidas do servidor

## Execução do código

1- Crie a rede Docker: `docker network create minha-rede`

2- Acesse `cd Desafio-1/Servidor` e dê build na imagem do servidor: `docker build -t meu-servidor .`

3- Acesse `cd Desafio-1/Cliente` e dê build na imagem do cliente: `docker build -t meu-cliente .`

4- Execute o container do servidor: `docker run -d --name server --network minha-rede -p 8080:8080 meu-servidor`

5- Execute o container do cliente: `docker run -d --name client --network minha-rede meu-cliente`

6- Ver os logs do cliente: `docker logs -f client`

7- Ver os logs do servidor: `docker logs -f server`


# Desafio 2

Este desafio monstra como dados podem persistir mesmo após a remoção de um container Docker, 
utilizando **volumes**. Foi utilizado o banco de dados **PostgreSQL**, armazenando os dados fora do container.

## Arquitetura

`docker-compose.yml`: Cria um container postgreSQL configurado, um volume persistente para armazenar os dados e uma rede docker

## Execução do código

1- Suba o container: `docker-compose up -d`

2- Tenha o PostgreSQL e entre nele: `docker exec -it meu_postgres psql -U admin -d exemplo_db`

3- No PostgreSQL vai aparecer a linha `exemplo_db=#`, nela crie a tabela, insira os dados e verifique se eles estão salvos: 

```bash
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome TEXT
);

INSERT INTO usuarios (nome) VALUES ('Arthur'), ('Maria'), ('João');
```

```bash
SELECT * FROM usuarios;
```

4- Abra outro terminal e derrube o container: `docker-compose down`

5- Depois, suba ele novamente: `docker-compose up -d`

6- Entre no banco novamente: `docker exec -it meu_postgres psql -U admin -d exemplo_db`

7- Na linha `exemplo_db=#`, veja os dados que persistiram:

```bash
SELECT * FROM usuarios;
```


# Desafio 3

Este desafio demonstra como organizar três serviços dependentes usando Docker Compose, **web** é a aplicação Flask em Python,
**db** é banco de dados PostgreSQL e **cache** que é o servidor Redis. Essa solução foi construída seguindo princípios de microsserviços em que cada componente tem responsabilidade única, é isolado e comunicam-se via rede interna criada automaticamente pelo Docker Compose.

## Arquitetura

## Execução do código


# Desafio 4

## Arquitetura

## Execução do código


# Desafio 5

## Arquitetura

## Execução do código