# Projeto2-FCCPD

# Desafio 1 

Este desafio consiste em criar dois containers Docker que se comunicam através de uma rede customizada.  
A solução utiliza um **servidor Flask** e um **cliente curl** para demonstrar a comunicação contínua entre os serviços.

## Arquitetura

A solução é composta por dois containers feitos nas pastas **Servidor** e **Cliente**:

### **Servidor (Flask)**

`app.py`: Executa a aplicação Flask na porta **8080** e responde requisições HTTP GET.

`Dockerfile`: Constroi a imagem localmente, instala as requisições do `requirements.txt` e por fim copia o codigo e executa o comando `python app.py`.

`requirements.txt`: Lista o que vai ser instalado no conteiner, que é o `Flask==3.0.0`.

### **Cliente (curl)**

`Dockerfile`: Executa um loop infinito chamando `http://server:8080` a cada 5 segundos e mostra no terminal as respostas recebidas do servidor.

## Execução do código

1- Crie a rede Docker: `docker network create minha-rede`

2- Acesse `cd Desafio-1/Servidor` e dê build na imagem do servidor: `docker build -t meu-servidor .`

3- Execute o container do servidor: `docker run -d --name server --network minha-rede -p 8080:8080 meu-servidor`

4- Ver os logs do servidor: `docker logs -f server`

5- Acesse `cd Desafio-1/Cliente` e dê build na imagem do cliente: `docker build -t meu-cliente .`

6- Execute o container do cliente: `docker run -d --name client --network minha-rede meu-cliente`

7- Ver os logs do cliente: `docker logs -f client`


# Desafio 2

Este desafio monstra como dados podem persistir mesmo após a remoção de um container Docker, 
utilizando **volumes**. Foi utilizado o banco de dados **PostgreSQL**, armazenando os dados fora do container.

## Arquitetura

`docker-compose.yml`: Cria um container postgreSQL configurado, um volume persistente para armazenar os dados e uma rede docker.

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
**db** é banco de dados PostgreSQL e **cache** que é o servidor Redis. Essa solução comunicam-se via rede interna criada automaticamente pelo Docker Compose.

## Arquitetura

Consiste de uma pasta chamada **Web** e um arquivo docker-compose.yml:

### **Web**

`app.py`: Executa a aplicação Flask que conecta no PostgreSQL e no Redis para depois testar os dois, e quando `http://localhost:5000` é acessado e mostra na tela a menssagem "Flask OK | Redis: pong | Postgres: mensagem salva!".

`Dockerfile`: Cria a imagem Docker do serviço Flask, copia o `requirements.txt` para dentro do container e por último copia o codigo e executa o comando `python app.py`.

`requirements.txt`: Lista o que vai ser instalado no conteiner, que é o `Flask==3.0.0`, o `psycopg2-binary` e o `redis`.

### **docker-compose.yml**

O `docker-compose.yml` organiza os serviços Flask (web), PostgreSQL (db) e Redis (cache) e configura suas dependências, ambiente e rede interna para que se comuniquem entre si.

## Execução do código

1- Suba o container: `docker-compose up -d`

2- Acesse o localhost:5000 para verificar se a menssagem "Flask OK | Redis: pong | Postgres: mensagem salva!" aparece: `http://localhost:5000` 

3- Acesse o banco de dados: `docker exec -it db-service psql -U user -d appdb`

4- Verifique se no banco de dados a tabela "menssagens" existe digitando na linha `appdb=#`:

```bash
\d mensagens;
```

6- Verifique se o banco está salvando a menssagem "Olá banco!" digitando na linha `appdb=#`:

```bash
SELECT * FROM mensagens;
```

7- Em outro terminal, verifique se o Redis está respondendo com a menssagem "PONG": `docker exec -it cache-service redis-cli ping`


# Desafio 4

Este desafio cria dois microsserviços independentes, **Servico-a** , que expõe uma API HTTP que retorna uma lista de usuários em JSON (/users) e **Servico-b**,que consulta **Servico-a** via HTTP, processa e combina dados e expõe um endpoint (/report) que apresenta as informações. Cada serviço tem seu próprio Dockerfile e roda em um container isolado. A comunicação entre serviços é direta via HTTP usando os nomes dos serviços como hostnames.

## Arquitetura

A solução é composta pelas pastas **Servico-a**, **Servico-b** e o arquivo **docker-compose.yml**:

### **Servico-a**

`app.py`: Executa um microsserviço usando Flask que retorna uma lista de usuários em formato JSON quando alguém acessa o endpoint `http://localhost:5001/users`.

`Dockerfile`: Cria a imagem Docker, copia o `requirements.txt` para dentro do container, diz ao Docker que o container usa a porta 5001 e por último copia o codigo e executa o comando `python app.py`.

`requirements.txt`: Lista o que vai ser instalado no conteiner, que é o `Flask==3.0.0`.

### **Servico-b**

`app.py`: Executa um microsserviço em Flask que faz uma requisição HTTP ao outro microsserviço criado, recebe a lista de usuários e gera um relatório em texto em `http://localhost:5002/report`.

`Dockerfile`:  Cria a imagem Docker, copia o `requirements.txt` para dentro do container, diz ao Docker que o container usa a porta 5002 e por último copia o codigo e executa o comando `python app.py`.

`requirements.txt`: Lista o que vai ser instalado no conteiner, que é o `Flask==3.0.0` e o `requests`.

### **docker-compose.yml**

O `docker-compose.yml` cria dois microsserviços, sobe cada um em seu próprio container, expõe suas portas, configura o `Servico-b` para chamar o `Servico-a` via variável de ambiente e faz com que o `Servico-a` suba primeiro.

## Execução do código

1- Suba o container: `docker-compose up -d`

2- Acesse o localhost:5001/users para ver se aparece "[{"active_since":"2021-04-10","id":1,"name":"Ana"},{"active_since":"2022-01-15","id":2,"name":"Bruno"},{"active_since":"2020-09-03","id":3,"name":"Carla"}]" na tela: `http://localhost:5001/users`

3- Acesse o localhost:5002  para ver se aparece "Usuário Ana — ativo desde 2021-04-10", "Usuário Bruno — ativo desde 2022-01-15" e
"Usuário Carla — ativo desde 2020-09-03" na tela: `http://localhost:5002/report`


# Desafio 5

## Arquitetura

## Execução do código