# main.py

# 1) 환경변수 불러오기
from dotenv import load_dotenv
load_dotenv()

# 2) OpenAI LLM 불러오기
from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI(model="gpt-4o-mini")  # 모델 명시

# 3) Streamlit UI
import streamlit as st

st.title("인공지능 시인 ")
subject = st.text_input("시의 주제를 입력해주세요.")

if subject:
    st.write(f"시의 주제 : {subject}")

if st.button("시 작성"):
    with st.spinner("시 작성중 ..."):
        prompt = f"'{subject}'에 대한 아름다운 시를 한국어로 4연 정도 써줘."
        result = chat_model.invoke(prompt)
        st.write(result.content)

