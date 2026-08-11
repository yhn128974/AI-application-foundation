import os
import dashscope
dashscope.base_http_api_url = "https://dashscope.aliyuncs.com/api/v1"

with open(r"C:\Users\YuEth\Desktop\AI综合学习方案\技术路线\Machine-learning-learning\prompt\04_资料\Day01\补充资料\06_金龙鱼_兰世立事件观点打标.md", "r", encoding="utf-8") as f:
    system_prompt = f.read()

messages = [
    {   "role": "system",
        "content": f"{system_prompt}"},
    {
        "role": "user",
        "content": "快吃瓜，兰世立正式宣战金龙鱼了,,兰世立挑战世界500强 金龙鱼，你的底线在哪里？ 我凭一个人 小 兰世立 中国东星集团有限公司总裁 1331630 LANSHILI @兰总说商业 以上为资讯，现在进行打标"
    }
    ]
response = dashscope.MultiModalConversation.call(
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    model='qwen3.6-flash',
    messages=messages,
    enable_thinking=False,
)
print(response.output.choices[0].message.content[0]["text"])
