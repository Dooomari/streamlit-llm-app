import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

def get_llm_response(user_input: str, expert_type: str) -> str:
    # 専門家ごとのシステムメッセージ
    system_messages = {
        "旅行コンシェルジュ": "あなたは優秀な旅行コンシェルジュです。旅行に関する質問に丁寧に回答してください。",
        "健康コンシェルジュ": "あなたは経験豊富な健康コンシェルジュです。健康に関する質問に丁寧に回答してください。"
    }
    system_message = system_messages.get(expert_type, "あなたは親切な専門家です。")
    chat = ChatOpenAI()
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_input)
    ]
    response = chat(messages)
    return response.content

st.title("コンシェルジュAIチャット")
st.write("ご希望のコンシェルジュを選択し、質問を入力してください。")


st.divider()
expert = st.radio("専門家を選択してください", ("旅行コンシェルジュ", "健康コンシェルジュ"))
user_input = st.text_input("質問を入力してください")
if st.button("送信"):
    if user_input:
        answer = get_llm_response(user_input, expert)
        st.write("AIの回答:", answer)
    else:
        st.warning("質問を入力してください。")
