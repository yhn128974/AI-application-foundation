from openai import OpenAI
import os

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://ws-tb5h1ovj9i2pokh3.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

messages=[
        {
            "role": "system", 
            "content": "You are a helpful assistant."},
        {
            "role":"user",
            "content":"请你介绍一下你自己",
            
        },
        # 模型上一次生成的内容， 给AI提供上下文参考
        {
            "role":"assistant",
            "content": "你好，我是一个AI助手很高兴为您服务喵~"
        },
        {
            "role": "user", 
            "content":"请你介绍一下你自己",
        # "content": [
        #     {
        #     "type": "image_url",
        #     # 给AI发送图像
        #      "image_url": {
        #         "url": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"
        #         }
        #      },
        #     {"type": "text", "text": "这是什么"},
        #     ]
        },
        
    ]
completion = client.chat.completions.create(
    model="qwen3.7-plus",  # 您可以按需更换为其它深度思考模型
    messages=messages,
    extra_body={"enable_thinking": False},
    stream=True
)

is_answering = False  # 是否进入回复阶段

print("\n" + "=" * 20 + "思考过程" + "=" * 20)


for chunk in completion:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta
    # 如果开启了深度思考，会输出 reasoning_content
    if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
        if not is_answering:
            print(delta.reasoning_content, end="", flush=True)
            
    # 正常输出content
    if hasattr(delta, "content") and delta.content:
        if not is_answering:
            print("\n" + "=" * 20 + "完整回复" + "=" * 20)
            is_answering = True
        print(delta.content, end="", flush=True)
    