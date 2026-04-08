# Chatbot com Inteligência Artificial

## Descrição
Este projeto consiste em um chatbot com inteligência artificial desenvolvido utilizando Python, Streamlit e a API da OpenAI.

## Funcionalidades
- Interface de chat interativa
- Comunicação com modelo de IA
- Histórico de conversas
- Respostas em tempo real

## Tecnologias utilizadas
- Python
- Streamlit
- OpenAI API

## Como funciona

O chatbot armazena o histórico da conversa e envia as mensagens para um modelo de linguagem (quando disponível).  
Caso não haja API configurada, o sistema utiliza um modo de demonstração com respostas simuladas.

## Como executar

1. Instale as dependências:
pip install -r requirements.txt


2. Configure sua chave da API:
Crie um arquivo `.env` e adicione:
OPENAI_API_KEY=sua_chave_aqui


3. Execute o projeto:
streamlit run main.py


## Estrutura do projeto
- `main.py`: aplicação principal do chatbot

## Objetivo
Demonstrar a integração de inteligência artificial em aplicações web interativas.

## 💬 Interface

![Chatbot](screenshot.png)
