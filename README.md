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