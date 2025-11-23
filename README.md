# Projeto2-FCCPD

# Desafio 1 

Este desafio consiste em criar dois containers Docker que se comunicam através de uma rede customizada.  
A solução utiliza um **servidor Flask** e um **cliente curl** para demonstrar a comunicação contínua entre os serviços.

## Arquitetura

A solução é composta por dois containers feitos nas pastas:

### **1. Servidor (Flask)**

app.py: Executa a aplicação Flask na porta **8080** e responde requisições HTTP GET em `/`

Dockerfile: Constroi a imagem localmente, instala as requisições do requirements.txt e por no fim copia o codigo e executa o comando python app.py

### **2. Cliente (curl)**

Dockerfile: Executa um loop infinito chamando `http://server:8080` a cada 5 segundos e mostra no terminal as respostas recebidas do servidor
