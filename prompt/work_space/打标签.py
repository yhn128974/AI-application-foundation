from openai import OpenAI
import os

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://ws-tb5h1ovj9i2pokh3.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

# 加载系统提示词
with open(r"prompt\04_资料\Day01\补充资料\06_金龙鱼_兰世立事件观点打标.md",'r',encoding='utf-8') as f:
    system_promt= f.read()

system_promt2="""
    要求：
        1. 从会议内容中提取行动项。
        2. 输出 JSON。
        3. 每个行动项包含 `item`、`owner`、`deadline`。
        4. 如果没有明确截止时间，`deadline` 写 `null`。
"""

system_promt3="""
    要求：
        1. 从一段需求描述中提取结构化信息。
        2. 输出 JSON，字段包含：
        `product`: 产品名称或类型
        `scenario`: 应用场景
        `channels`: 渠道/平台
        `constraints`: 约束/要求
        `risk_handling`: 风险处理方式
"""


user_input_text = """ 
我们想做一个 AI 客服助手，主要用于回答用户关于订单、退款、物流的问题。
希望先接入网页端，输出要简洁，遇到不确定的问题要提示转人工。
"""

user_input_text2 = """ 
我们想做一个智能语音助手，通过语音控制智能家居，主要用于调节灯光、温度、窗帘等设备。
先接入卧室场景，语音要尽量自然口语化，遇到没听懂的语音要礼貌地问用户重复一遍。
"""


messages=[
        {   
            "role": "system", 
            "content": f"{system_promt3}"},
        {
            "role":"user",
            "content": f"{user_input_text2}"
        }
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


