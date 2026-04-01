# AtlasShop Assist
Assistente conversacional desenvolvido para responder perguntas com base em dados estruturados e documentos internos, utilizando uma API em FastAPI e uma interface web simples.

## Visão Geral
O AtlasShop Assist é um projeto de IA conversacional criado como desafio técnico, com o objetivo de simular um assistente de atendimento capaz de:
- consultar informações de clientes
- consultar status de pedidos
- verificar reembolsos
- responder perguntas com base em documentos da base de conhecimento

## Funcionalidades
- Consulta de clientes por ID
- Consulta de pedidos por ID
- Verificação de reembolso por pedido
- Busca em documentos com fallback via RAG simples
- Interface web para envio de perguntas
- Orquestração baseada em regras

## Tecnologias Utilizadas
- Python 3.14
- FastAPI
- Pandas
- HTML
- CSS
- JavaScript
- Bootstrap

###### Como Executar o Projeto

## 1. Extrair o projeto
- Baixe o arquivo `.zip`
- Extraia o conteúdo em uma pasta local

 ## 2. Abrir o projeto
- Abra a pasta do projeto no VS Code ou terminal

## 3. Criar e ativar ambiente virtual

- Windows
python -m venv .venv
.venv\Scripts\activate

- Linux/Mac
python3 -m venv .venv
source .venv/bin/activate

 ## 4. Instalar dependencias 
pip install -r requirements.txt

## 5.Executar a aplicação
uvicorn app.main:app --reload

## Acessar no navegador
- aplicação
http://127.0.0.1:8000

- documentação API
http://127.0.0.1:8000/docs


## Como usar
Digite uma pergunta no campo de texto ou utilize os exemplos disponíveis na interface.
O sistema irá:
- consultar dados estruturados (clientes, pedidos, reembolsos)
- ou buscar informações na base documental (knowledge/)

