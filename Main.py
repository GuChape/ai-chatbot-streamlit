import streamlit as st
import os

# Configuração da página
st.set_page_config(page_title="Chatbot IA", layout="centered")

st.title("🤖 Chatbot com Inteligência Artificial")

# Memória do chat
if "mensagens" not in st.session_state:
    st.session_state["mensagens"] = []

# Exibir mensagens antigas
for msg in st.session_state["mensagens"]:
    st.chat_message(msg["role"]).write(msg["content"])

# Input do usuário
mensagem_usuario = st.chat_input("Digite sua mensagem...")

if mensagem_usuario:
    # Mostra mensagem do usuário
    st.chat_message("user").write(mensagem_usuario)
    st.session_state["mensagens"].append({
        "role": "user",
        "content": mensagem_usuario
    })

    # Verifica se tem API
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        from openai import OpenAI
        cliente = OpenAI(api_key=api_key)

        resposta = cliente.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state["mensagens"]
        )

        resposta_ia = resposta.choices[0].message.content

    else:
        # MODO DEMO (SEM API)
        resposta_ia = f"🤖 (Modo demo) Você disse: {mensagem_usuario}"

    # Mostrar resposta
    st.chat_message("assistant").write(resposta_ia)

    st.session_state["mensagens"].append({
        "role": "assistant",
        "content": resposta_ia
    })