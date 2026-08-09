# Python 大模型提示词 Day01 作业

## 一、选择题

1. 人工智能发展的三个核心驱动力是？

A. 数据、算法、算力  
B. 电脑、鼠标、键盘  
C. 前端、后端、数据库  
D. 图片、视频、音频

2. 关于提示词的说法，正确的是？

A. 提示词只等于用户最后输入的问题  
B. 提示词可以包含角色、规则、资料、示例和输出格式  
C. 提示词越短越好，不能写长  
D. 提示词只在网页聊天中有用，代码调用时没有用

3. 下面哪种情况更像事实性幻觉？

A. 要求只输出 JSON，模型多输出解释  
B. 模型把不存在的公司新闻说成真实发生  
C. 模型回复太长  
D. 模型没有使用表格

4. 下面哪种情况更像忠实性幻觉？

A. 模型没有遵守“只输出 JSON”的要求  
B. 模型说了一个错误年份  
C. 模型编造了不存在的人名  
D. 模型把别人的作品说成某歌手作品

5. RAG 更适合解决什么问题？

A. 让模型改变底层参数  
B. 让模型检索外部资料后再回答  
C. 让模型自动点击网页  
D. 让模型不需要提示词

6. 微调更像下面哪种说法？

A. 给模型一份临时参考资料  
B. 让模型回炉深造，长期学习某类能力  
C. 让模型调用天气接口  
D. 让模型把回答变短

7. Agent 的核心理解是？

A. 模型只负责生成图片  
B. 模型做决策，程序负责调用工具执行  
C. 模型不能和程序结合  
D. Agent 等于普通聊天窗口

8. 在 `messages` 中，`system` 角色主要用于？

A. 提供模型身份、规则和输出边界  
B. 表示用户本次提问  
C. 表示数据库连接  
D. 表示 Python 文件名

9. API Key 的正确使用方式是？

A. 直接写进代码并发给同学  
B. 截图发到群里方便大家复制  
C. 放到环境变量或安全配置中读取  
D. 随便写一个字符串即可

10. 为什么很多 AI 项目要求模型输出 JSON？

A. JSON 看起来更复杂  
B. JSON 方便程序继续解析和处理  
C. JSON 只能给人阅读  
D. JSON 可以自动训练模型

## 二、填空题

1. AI 能力的三个核心驱动力是 ________、________、________。

2. 大模型幻觉可以分为 ________ 幻觉和 ________ 幻觉。

3. 提示词包含用户问题，但不等于 ________。

4. RAG 可以用“________ 考试”来类比，因为它会给模型提供外部资料。

5. 微调可以理解为让模型 ________，从而长期适配某类任务。

6. Agent 中，模型主要负责 ________，程序主要负责 ________。

7. `messages` 中常见的三个角色是 ________、________、________。

8. `system` 角色通常用于设定模型的身份、任务规则和 ________。

9. API Key 不应该写进公开代码，推荐放到 ________ 中。

10. 如果希望程序更容易处理模型结果，可以要求模型输出 ________ 格式。

## 三、简答题

1. 为什么说提示词不是简单的一句用户提问？

2. 请用自己的话解释事实性幻觉。

3. 请用自己的话解释忠实性幻觉。

4. RAG 和微调有什么区别？

5. 为什么工作中经常要求模型输出 JSON？

6. `system`、`user`、`assistant` 三种角色分别有什么作用？

7. 为什么 API Key 不能直接写在代码里？

8. 请列出一个清晰提示词应该包含的 4 个要素。

9. 什么情况下适合给模型提供示例？

10. 为什么复杂任务要拆成多个步骤再交给模型？

## 四、代码实操题

### 1. 基础练习：调用模型完成一句话解释

要求：

1. 使用 OpenAI 兼容方式调用模型。
2. 从环境变量读取 `OPENAI_API_KEY`。
3. 提问：“请用一句话解释提示词工程。”
4. 打印模型回复。

### 2. 基础练习：设置计算器角色

要求：

1. 使用 OpenAI 兼容方式调用模型。
2. `system` 中设定：你是一个计算器，只输出最终结果，不要解释。
3. `user` 中提问：`2 + 5 * 3 等于多少？`
4. 打印模型回复。

### 3. 基础练习：DashScope 调用模型

要求：

1. 使用 `dashscope` 库调用模型。
2. 从环境变量读取 `DASHSCOPE_API_KEY`。
3. 提问：“请用一句话解释 RAG。”
4. 打印模型回复。

### 4. 进阶练习：客户反馈情绪分类

要求：

1. 使用 `system` 设定模型为客户反馈分析助手。
2. 输入一段客户反馈。
3. 要求输出 JSON，字段包含 `emotion`、`problem`、`suggestion`。
4. 情绪只能是：正面、负面、中性。

客户反馈：

```text
这个 AI 写作工具生成速度挺快，但是经常答非所问，导出的格式也有点乱。
```

### 5. 进阶练习：会议行动项提取

要求：

1. 从会议内容中提取行动项。
2. 输出 JSON。
3. 每个行动项包含 `item`、`owner`、`deadline`。
4. 如果没有明确截止时间，`deadline` 写 `null`。

会议内容：

```text
本次周会决定，小王本周五前完成智能客服原型页面，小张负责整理客户反馈，但没有明确截止时间。
```

### 6. 进阶练习：给模型一个示例

要求：

1. 使用 `system` 设定模型为信息抽取助手。
2. 给模型提供一个 `user` 示例和一个 `assistant` 示例。
3. 再提供真正要处理的文本。
4. 输出姓名、手机号、地址 JSON。

### 7. 综合案例：社媒内容分类

要求：

设计一个社媒内容分类提示词，将输入内容分为：

- 噪音
- 广告营销
- 弱相关
- 非噪音

要求：

1. 使用 `system` 写清分类规则。
2. 使用 `user` 输入待分类内容。
3. 输出 JSON，字段包含 `label`、`confidence`。

测试内容：

```text
#海底捞# 今天生日去吃饭，服务员送了蛋糕，体验很好！
```

### 8. 综合案例：AI 产品需求整理

要求：

从一段需求描述中提取结构化信息。

输入：

```text
我们想做一个 AI 客服助手，主要用于回答用户关于订单、退款、物流的问题。
希望先接入网页端，输出要简洁，遇到不确定的问题要提示转人工。
```

输出 JSON，字段包含：

- `product`
- `scenario`
- `channels`
- `constraints`
- `risk_handling`

## 五、选择题答案

1. A
2. B
3. B
4. A
5. B
6. B
7. B
8. A
9. C
10. B

## 六、填空题答案

1. 数据、算法、算力
2. 事实性、忠实性
3. 用户问题
4. 开卷
5. 回炉深造
6. 决策、调用工具执行
7. system、user、assistant
8. 输出边界
9. 环境变量
10. JSON

## 七、简答题参考答案

1. 因为真实提示词除了用户问题，还可能包含角色设定、业务背景、参考资料、示例、步骤、输出格式和边界规则。用户问题只是提示词的一部分。

2. 事实性幻觉指模型生成的内容和现实事实不一致，比如编造不存在的事件、人物、作品或时间。

3. 忠实性幻觉指模型没有遵守用户指令或上下文要求，比如要求只输出 JSON，它却额外输出解释。

4. RAG 是检索外部资料后交给模型回答，像开卷考试；微调是对模型进行二次训练或参数调整，让模型长期适配某类任务。

5. 因为 JSON 字段固定，程序容易解析，可以继续写入数据库、传给前端或进入工作流。

6. `system` 用来设定规则和边界；`user` 用来提出具体问题；`assistant` 表示模型回复，常用于提供示例答案。

7. 因为 API Key 相当于账户钥匙，泄露后别人可能消耗额度或造成安全风险。应该放到环境变量或安全配置中读取。

8. 可以包含角色、任务、背景、约束、输出格式、示例、参考资料等，答出其中 4 个即可。

9. 当希望模型模仿固定格式、风格、分类标准或输出结构时，适合提供示例。

10. 因为复杂任务一次性提交容易让模型遗漏步骤或误解意图，拆步骤可以降低难度，让模型按流程完成任务。

## 八、代码实操参考答案

### 1. 基础练习：调用模型完成一句话解释

```python
"""
需求：
    使用 OpenAI 兼容方式调用云端模型，让模型用一句话解释提示词工程。

步骤：
    1. 导入 os 和 OpenAI。
    2. 从环境变量读取 OPENAI_API_KEY，避免把真实密钥写进代码。
    3. 创建 OpenAI 客户端，并指定阿里百炼兼容接口地址。
    4. 准备 messages，提交系统规则和用户问题。
    5. 获取模型回复并打印。
"""

import os  # 用来读取系统环境变量
from openai import OpenAI  # 用来创建模型调用客户端


api_key = os.getenv("OPENAI_API_KEY")  # 从环境变量读取密钥
if not api_key:
    # 如果没有读取到密钥，直接抛出清晰错误，方便排查
    raise ValueError("没有读取到 OPENAI_API_KEY，请配置环境变量后重启 PyCharm。")

client = OpenAI(
    api_key=api_key,  # 平台通过密钥识别调用者身份
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 阿里百炼兼容接口地址
)

completion = client.chat.completions.create(
    model="qwen-plus",  # 指定模型，实际可用模型以平台列表为准
    messages=[
        {
            "role": "system",
            "content": "你是一个简洁的 AI 助手，请用中文回答。"
        },
        {
            "role": "user",
            "content": "请用一句话解释提示词工程。"
        }
    ]
)

print(completion.choices[0].message.content)  # 打印第一条模型回复
```

### 2. 基础练习：设置计算器角色

```python
"""
需求：
    设定模型为计算器，让它只输出最终计算结果。

步骤：
    1. 读取 API Key。
    2. 创建客户端。
    3. 在 system 中限定模型角色和输出规则。
    4. 在 user 中提出计算问题。
"""

import os
from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("没有读取到 OPENAI_API_KEY，请配置环境变量后重启 PyCharm。")

client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {
            "role": "system",
            # system 用来定规则：这里明确要求模型像计算器一样，只输出结果
            "content": "你是一个计算器，只输出最终计算结果，不要解释过程。"
        },
        {
            "role": "user",
            # user 是本次真正要处理的问题
            "content": "2 + 5 * 3 等于多少？"
        }
    ]
)

print(completion.choices[0].message.content)
```

### 3. 基础练习：DashScope 调用模型

```python
"""
需求：
    使用 dashscope 库调用阿里通义模型，解释 RAG。

步骤：
    1. 导入 os 和 dashscope。
    2. 从环境变量读取 DASHSCOPE_API_KEY。
    3. 调用 Generation.call。
    4. 从 response.output["text"] 中取出模型回复。
"""

import os
import dashscope


dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")  # 设置 SDK 调用密钥
if not dashscope.api_key:
    raise ValueError("没有读取到 DASHSCOPE_API_KEY，请配置环境变量后重启 PyCharm。")

response = dashscope.Generation.call(
    model="qwen-plus",
    messages=[
        {
            "role": "system",
            "content": "你是一个简洁的 AI 助手，请用中文回答。"
        },
        {
            "role": "user",
            "content": "请用一句话解释 RAG。"
        }
    ]
)

print(response.output["text"])
```

### 4. 进阶练习：客户反馈情绪分类

```python
"""
需求：
    从客户反馈中判断情绪、提取问题，并给出回复建议。

步骤：
    1. system 中写清模型身份、分类范围和输出格式。
    2. user 中放入客户反馈。
    3. 要求模型只输出 JSON，方便程序继续处理。
"""

import os
from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("没有读取到 OPENAI_API_KEY，请配置环境变量后重启 PyCharm。")

client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

system_prompt = """
你是一个客户反馈分析助手。
请分析用户反馈，并输出 JSON。

要求：
1. emotion 只能是：正面、负面、中性。
2. problem 提取客户提到的主要问题。
3. suggestion 给出一句适合客服回复的建议。
4. 只输出 JSON，不要输出解释文字。
"""

user_feedback = """
这个 AI 写作工具生成速度挺快，但是经常答非所问，导出的格式也有点乱。
"""

completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_feedback},
    ]
)

print(completion.choices[0].message.content)
```

### 5. 进阶练习：会议行动项提取

```python
"""
需求：
    从会议内容中提取行动项，输出可被程序解析的 JSON。

步骤：
    1. 定义提取规则。
    2. 指定每个行动项必须包含 item、owner、deadline。
    3. 对没有截止时间的任务，要求 deadline 使用 null。
"""

import os
from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("没有读取到 OPENAI_API_KEY，请配置环境变量后重启 PyCharm。")

client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

system_prompt = """
你是一个会议行动项提取助手。
请从会议内容中提取明确有人负责的任务。

输出要求：
1. 只输出 JSON。
2. JSON 顶层字段为 action_items。
3. 每个行动项包含 item、owner、deadline。
4. 如果没有明确截止时间，deadline 写 null。
"""

meeting_text = """
本次周会决定，小王本周五前完成智能客服原型页面，小张负责整理客户反馈，但没有明确截止时间。
"""

completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": meeting_text},
    ]
)

print(completion.choices[0].message.content)
```

### 6. 进阶练习：给模型一个示例

```python
"""
需求：
    使用 few-shot 示例，让模型学习快递信息抽取的输入和输出格式。

步骤：
    1. system 设定任务规则。
    2. user 提供一个示例输入。
    3. assistant 提供一个示例输出。
    4. user 提供真正要处理的新输入。
"""

import os
from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("没有读取到 OPENAI_API_KEY，请配置环境变量后重启 PyCharm。")

client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

system_prompt = """
你是一个快递信息提取助手。
请提取姓名、手机号、地址。
只输出 JSON。
手机号中的横线和空格要去掉。
"""

example_user = """
张明远，138-1234-5678
广东省深圳市南山区科技园南区高新南一道1000号腾讯大厦18层 1806室
"""

example_assistant = """
{"name": "张明远", "phone": "13812345678", "address": "广东省深圳市南山区科技园南区高新南一道1000号腾讯大厦18层 1806室"}
"""

real_user = """
李婉婷
151-9876-5432
北京市海淀区中关村大街1号海龙大厦8层805室
东西是一份文件，已经封装好了。
"""

completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": example_user},
        {"role": "assistant", "content": example_assistant},
        {"role": "user", "content": real_user},
    ]
)

print(completion.choices[0].message.content)
```

### 7. 综合案例：社媒内容分类

```python
"""
需求：
    将社媒内容分类为噪音、广告营销、弱相关、非噪音。

步骤：
    1. 在 system 中写清四个标签的判断规则。
    2. 在 user 中输入待分类文本。
    3. 要求模型输出 label 和 confidence。
"""

import os
from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("没有读取到 OPENAI_API_KEY，请配置环境变量后重启 PyCharm。")

client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

system_prompt = """
你是一个品牌社媒内容分类助手。

请将输入内容分类为以下四类之一：
1. 噪音：完全无关，比如成语、误匹配、人名等。
2. 广告营销：促销、打卡、优惠、正面分享。
3. 弱相关：只是顺带提到品牌，没有具体行为或评价。
4. 非噪音：真实评价、投诉、体验、负面内容或有效内容。

输出要求：
1. 只输出 JSON。
2. label 必须是：噪音、广告营销、弱相关、非噪音。
3. confidence 必须是：high、medium、low。
"""

content = "#海底捞# 今天生日去吃饭，服务员送了蛋糕，体验很好！"

completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": content},
    ]
)

print(completion.choices[0].message.content)
```

### 8. 综合案例：AI 产品需求整理

```python
"""
需求：
    从一段 AI 产品需求描述中提取结构化信息。

步骤：
    1. system 中规定字段和输出要求。
    2. user 中输入原始需求。
    3. 输出 JSON，方便后续写入需求文档或传给工作流。
"""

import os
from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("没有读取到 OPENAI_API_KEY，请配置环境变量后重启 PyCharm。")

client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

system_prompt = """
你是一个 AI 产品需求分析助手。
请从用户输入中提取结构化需求信息。

输出 JSON，字段包括：
1. product：产品名称或产品类型。
2. scenario：主要应用场景。
3. channels：使用渠道，数组格式。
4. constraints：约束条件，数组格式。
5. risk_handling：风险处理方式。

只输出 JSON，不要输出解释文字。
"""

requirement = """
我们想做一个 AI 客服助手，主要用于回答用户关于订单、退款、物流的问题。
希望先接入网页端，输出要简洁，遇到不确定的问题要提示转人工。
"""

completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": requirement},
    ]
)

print(completion.choices[0].message.content)
```

