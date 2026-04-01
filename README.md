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

## Estrutura do Projeto
```bash
atlasshop-assist/
├── app/
│   ├── main.py
│   ├── orchestrator.py
│   ├── rag.py
│   └── tools.py
├── data/
│   ├── clientes.csv
│   ├── pedidos.csv
│   └── reembolsos.csv
├── knowledge/
│   ├── catalogo_planos.md
│   ├── comunicados_incidentes.md
│   ├── faq_atendimento.md
│   ├── playbook_escalonamento.md
│   ├── politica_cancelamento_reembolso_antiga.md
│   └── politica_cancelamento_reembolso_atual.md
├── public/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── docs/
│   └── documentacao_tecnica.md
├── requirements.txt
└── README.md