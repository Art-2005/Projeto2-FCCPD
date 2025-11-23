# Projeto2-FCCPD

# Desafio 1 

Este desafio consiste em criar dois containers Docker que se comunicam através de uma rede customizada.  
A solução implementada utiliza um **servidor Flask** e um **cliente curl** para demonstrar a comunicação contínua entre os serviços.

## Arquitetura da Solução

A solução é composta por dois containers:

### **1. Servidor (Flask)**
- Executa uma aplicação Flask na porta **8080**
- Responde requisições HTTP GET em `/`
- Imagem construída localmente com um Dockerfile simples

### **2. Cliente (curl)**
- Container minimalista baseado em `curlimages/curl`
- Executa um loop infinito chamando `http://server:8080` a cada 5 segundos
- Mostra no terminal as respostas recebidas do servidor

### **3. Rede Docker**
- Uma rede do tipo `bridge` chamada **minha-rede**
- Ambos os containers estão conectados a essa rede
- Permite comunicação pelo nome DNS do container (ex: `server`)