import streamlit as st
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

system_prompt = "You are a helpful assistant"

if "messges" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])
        


# print(response.choices[0].message.content)

# 页面配置
st.set_page_config(
    page_title="Ai 智能伴侣", 
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.streamlit.io/help',  }
)
# 标题
st.title("AI智能伴侣")
# 
st.logo("./logo.png")
# 


# 消息输入框
user_input = st.text_input("请输入消息：")
if user_input:
    st.chat_message("user").write(user_input)
   
    # 模型输出
    response = client.chat.completions.create( 
        model="deepseek-v4-pro",
        messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content":user_input }
        ],
        stream=False,
        # reasoning_effort="high",
        # extra_body={"thinking": {"type": "enabled"}}
 )

    st.chat_message("assistant").write(response.choices[0].message.content)
    st.success("消息已发送！")
    # messages.append({"role": "user", "content": user_input})

    

