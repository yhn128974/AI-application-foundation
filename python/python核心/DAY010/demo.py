# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
import requests
import json

# import requests
#
# url = "https://chat.cqjtu.edu.cn/ds/api/v1/models"
#
# payload={}
# headers = {
#   'Accept': 'application/json',
#   'Authorization': 'Bearer sk-90b6c33070041bb984b167dd8884e729'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)



# url = "https://chat.cqjtu.edu.cn/ds/api/v1/chat/completions"
#
# payload = json.dumps({
#   "messages": [
#     {
#       "content": "You are a helpful assistant",
#       "role": "system"
#     },
#     {
#       "content": "Hi can you give me some message?",
#       "role": "user"
#     }
#   ],
#   "model": "deepseek-chat",
#   "frequency_penalty": 0,
#   "max_tokens": 2048,
#   "presence_penalty": 0,
#   "response_format": {
#     "type": "text"
#   },
#   "stop": None,
#   "stream": False,
#   "stream_options": None,
#   "temperature": 1,
#   "top_p": 1,
#   "tools": None,
#   "tool_choice": "none",
#   "logprobs": False,
#   "top_logprobs": None
# })
#
# headers = {
#   'Content-Type': 'application/json',
#   'Accept': 'application/json',
#   'Authorization': 'Bearer sk-90b6c33070041bb984b167dd8884e729'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)




client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)