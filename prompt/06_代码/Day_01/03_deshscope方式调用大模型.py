import os
import dashscope
dashscope.base_http_api_url = "https://dashscope.aliyuncs.com/api/v1"

messages = [
        {
            "role": "system",
            "content": "你是一名专业的电商客服，回答要礼貌、简洁、有帮助。"
        },
        {
            "role": "user",
            "content": "我买的平板屏幕有划痕，能换吗？"
        }
    ]
'''
messages = [
    {
      "role": "system",
      "content": "你是一名专业的电商客服，回答要礼貌、简洁、有帮助。"
    },
    {
      "role": "user", 
      "content": "我买的手机屏幕有划痕，能换吗？"
    },
    {
      "role": "assistant",
      "content": "非常抱歉给您带来不便。手机屏幕划痕属于外观问题，请在签收后24小时内联系我们处理。您已使用三天，建议联系官方售后检测。需要我帮您转接售后吗？"
    },
    {
        "role": "user",
        "content": "我买的平板屏幕有划痕，能换吗？"
    }
    ]
    
'''
response = dashscope.MultiModalConversation.call(
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    model='qwen3.7-plus',
    messages=messages
)
print("结果为：\n")
print(response)
print(response.output.choices[0].message.content[0]["text"])



'''
response = dashscope.MultiModalConversation.call(
    # 必需参数
    api_key=os.getenv('DASHSCOPE_API_KEY'),  # API密钥
    model='qwen3.7-plus',                    # 模型名称
    messages=messages,                       # 对话消息
    
    # 可选参数
    # 1. 生成控制参数
    temperature=0.85,        # 温度参数 (0-2)，控制随机性，默认0.85
    top_p=0.8,              # 核采样阈值 (0-1)，默认0.8
    top_k=10,               # Top-K采样，默认None
    max_tokens=1500,        # 最大生成token数
    seed=1234,              # 随机种子，用于可复现生成
    
    # 2. 停止控制
    stop=None,              # 停止词列表，如 ["。", "？"]
    
    # 3. 重复控制
    repetition_penalty=1.0, # 重复惩罚因子 (1.0-2.0)
    
    # 4. 结果数量
    n=1,                    # 返回的结果数量
    
    # 5. 流式输出
    stream=False,          # 是否流式返回
    incremental_output=False,  # 流式输出时是否增量返回
    
    # 6. 其他高级参数
    enable_search=False,   # 是否启用联网搜索
    result_format='message',  # 返回格式: 'message' 或 'text'
    
    # 7. 工作空间
    workspace=None,        # 工作空间ID
    
    # 8. 超时设置
    timeout=30,            # 请求超时时间（秒）
)
'''


"""
{
  "messages": [
    {
      "role": "system",
      "content": "你是一名专业的电商客服，回答要礼貌、简洁、有帮助。"
    },
    {
      "role": "user", 
      "content": "我买的手机屏幕有划痕，能换吗？"
    },
    {
      "role": "assistant",
      "content": "非常抱歉给您带来不便。手机屏幕划痕属于外观问题，请在签收后24小时内联系我们处理。您已使用三天，建议联系官方售后检测。需要我帮您转接售后吗？"
    }
  ]
}

"""


"""
response = dashscope.Generation.call(
    model='qwen-max',
    messages=[
    {
      "role": "system",
      "content": "你是一名专业的电商客服，回答要礼貌、简洁、有帮助。"
    },
    {
      "role": "user", 
      "content": "我买的手机屏幕有划痕，能换吗？"
    },
    {
      "role": "assistant",
      "content": "非常抱歉给您带来不便。手机屏幕划痕属于外观问题，请在签收后24小时内联系我们处理。您已使用三天，建议联系官方售后检测。需要我帮您转接售后吗？"
    },
    {
      "role": "user", 
      "content": "我买的平板屏幕有划痕，能换吗？"
    }
    
    ]
)



"""

"""
非常抱歉给您带来不便。平板屏幕划痕与手机规则一致，属于外观问题。
签收24小时内可联系我们处理，若已签收使用，建议联系官方售后检测。
请问您的平板签收多久了？需要帮您转接售后吗？
"""


"""
您好！非常抱歉给您带来不便。平板屏幕有划痕是可以申请售后的，具体能否直接换货，需要看您的**收货时间**和**划痕情况**。

为了尽快帮您解决，麻烦您提供以下信息：
1. 您的**订单号**。
2. 屏幕划痕的**清晰照片**。

💡 **售后小贴士**：
* **刚签收发现**：如果是收到货时就发现有划痕（非人为），在退换货期限内（通常7天无理由/15天质量问题），我们可以为您办理换货或退货。
* **使用后产生**：如果是使用过程中不慎造成的划痕，通常无法直接免费换新，但我们可以帮您联系官方提供维修或换屏方案。

请您把照片和订单号发给我，我会立刻为您核实并提供最合适的处理方案！
"""