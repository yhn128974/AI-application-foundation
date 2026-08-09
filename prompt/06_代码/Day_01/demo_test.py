# from openai import OpenAI
# import os
#
# client = OpenAI(
#     # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
#     api_key=os.getenv("DASHSCOPE_API_KEY"),
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
# )
#
# messages = [{"role": "user", "content": "你是谁"}]
# completion = client.chat.completions.create(
#     model="qwen3.7-plus",  # 您可以按需更换为其它深度思考模型
#     messages=messages,
#     extra_body={"enable_thinking": False},
#     stream=True
# )
# is_answering = False  # 是否进入回复阶段
# print("\n" + "=" * 20 + "思考过程" + "=" * 20)
# for chunk in completion:
#     if not chunk.choices:
#         continue
#     delta = chunk.choices[0].delta
#
#     if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
#         if not is_answering:
#             print(delta.reasoning_content, end="", flush=True)
#     if hasattr(delta, "content") and delta.content:
#         if not is_answering:
#             print("\n" + "=" * 20 + "完整回复" + "=" * 20)
#             is_answering = True
#         print(delta.content, end="", flush=True)


import os
import dashscope
dashscope.base_http_api_url = "https://dashscope.aliyuncs.com/api/v1"

messages = [
    {
        "role": "user",
        "content": "当小明 6 岁时，他的妹妹的年龄是他的一半。他的哥哥比小明大 4 岁。现在小明 70 岁了，请问他的妹妹和哥哥的年龄加起来是多少？"
    }
    ]
response = dashscope.MultiModalConversation.call(
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    model='qwen3.6-flash',
    messages=messages,
    enable_thinking=False
)
print(response.output.choices[0].message.content[0]["text"])


# pip install dashscope
# pip install openai



