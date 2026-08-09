# Day02 大模型提示词课后作业

## 一、选择题

1. 在真实项目中，使用 Python 调用大模型 API 的主要目的是什么？

   A. 让学生少写代码  
   B. 让程序自动把问题发送给模型并处理结果  
   C. 替代所有数据库操作  
   D. 让模型自动保存 API Key

2. `api_key` 的主要作用是？

   A. 指定模型名称  
   B. 指定输出语言  
   C. 证明调用者有权限访问模型服务  
   D. 控制是否流式输出

3. `base_url` 的主要作用是？

   A. 指定请求发往哪个模型服务地址  
   B. 指定用户输入内容  
   C. 指定返回结果的字体  
   D. 指定代码文件保存路径

4. 关于批处理和流式输出，下列说法正确的是？

   A. 批处理必须使用 `stream=True`  
   B. 流式输出会一次性返回完整答案  
   C. 批处理通常一次性返回完整结果  
   D. 流式输出不能用于聊天场景

5. 在 OpenAI 兼容接口中开启流式输出的常见参数是？

   A. `fast=True`  
   B. `stream=True`  
   C. `flow=False`  
   D. `print=True`

6. zero-shot 的含义是？

   A. 给模型很多示例  
   B. 不给示例，直接让模型完成任务  
   C. 训练一个新模型  
   D. 删除所有提示词

7. few-shot 更适合下列哪个场景？

   A. 固定格式的文本分类  
   B. 关闭电脑  
   C. 修改 Python 解释器  
   D. 安装操作系统

8. CoT 思维链最适合用于？

   A. 简单问候  
   B. 简单翻译一个词  
   C. 多步骤推理问题  
   D. 输出当前时间

9. ReAct 中的 Action 指什么？

   A. 模型输出最终答案  
   B. 模型决定调用某个工具或执行某个动作  
   C. 程序删除提示词  
   D. 用户关闭浏览器

10. 提示词注入攻击的典型特征是？

    A. 用户输入中包含试图覆盖原始规则的恶意指令  
    B. 用户正常提问天气  
    C. 程序正常读取环境变量  
    D. 模型正常返回 JSON

## 二、填空题

1. 大模型 API 调用的四个基本步骤是：导包、________、发送消息、________。

2. `messages` 是大模型接口中的 ________ 列表。

3. OpenAI 兼容接口的好处是可以用类似写法调用不同平台的 ________。

4. 流式输出通常需要使用 ________ 循环逐段读取模型返回内容。

5. `end=""` 的作用是让 `print()` 打印后不自动 ________。

6. zero-shot 表示不给模型 ________，直接让模型完成任务。

7. few-shot 表示给模型少量 ________，让模型模仿格式或判断标准。

8. CoT 的中文名称是 ________。

9. Self-Consistency 可以理解为多条思路生成答案后进行 ________ 或比较。

10. ReAct 的核心循环可以概括为：思考、行动、________、再思考。

## 三、简答题

1. 为什么真实项目中不能只依赖网页端和大模型聊天？

2. 批处理和流式输出有什么区别？

3. 如果模型返回结果取不到，应该如何排查？

4. zero-shot 和 few-shot 的区别是什么？

5. few-shot 为什么不是训练模型？

6. CoT 适合什么任务？为什么简单任务不一定适合 CoT？

7. 链式提示和 CoT 有什么区别？

8. Self-Consistency 的优点和代价分别是什么？

9. ReAct 中模型和程序分别负责什么？

10. 提示词注入攻击应该如何防御？

## 四、代码实操题

### 1. 大模型基础调用

编写代码，使用 OpenAI 兼容接口调用云端模型，让模型回答：“请用三句话说明 Python 程序员为什么要学习大模型 API 调用。”

要求：

1. 使用 `OpenAI` 客户端。
2. 使用 `messages` 传入用户问题。
3. 打印模型回答。

### 2. 流式输出

在上一题基础上，开启流式输出，让模型逐段输出内容。

要求：

1. 使用 `stream=True`。
2. 使用 `for` 循环读取片段。
3. 使用 `end=""` 和 `flush=True`。

### 3. Few-shot 翻译

编写代码，让模型根据一个英文到中文的示例，翻译新的英文句子。

要求：

1. 在 `system` 中提供一个翻译示例。
2. 在 `user` 中提供新的英文句子。
3. 打印模型返回的中文翻译。

### 4. Zero-shot CoT

编写代码，让模型回答年龄题，并要求它一步一步思考。

题目：

```text
当小明 6 岁时，他的妹妹年龄是他的一半。他的哥哥比小明大 4 岁。
现在小明 70 岁了，请问他的妹妹和哥哥年龄加起来是多少？
```

要求：

1. 在提示词中加入“请一步一步思考”。
2. 打印模型的推理过程和最终答案。

### 5. 链式提示

编写代码，完成三步链式任务：

1. 从一段文本中抽取要点。
2. 根据要点写摘要。
3. 优化摘要语言。

要求：

1. 前一步结果要作为下一步输入。
2. 每一步都打印结果。

### 6. Self-Consistency 简化实现

编写代码，让模型针对同一个问题生成 3 个不同思路，再让模型从多个答案中选出最合理的结果。

要求：

1. 不使用 `eval()` 解析模型返回内容。
2. 代码中说明为什么不建议使用 `eval()`。
3. 最终打印投票或评审后的结果。

### 7. ReAct 简化工具调用

编写一个简化版 ReAct 程序，完成天气查询任务。

要求：

1. 提供一个 `get_weather(city)` 函数，模拟查询天气。
2. 让模型先判断需要查询哪个城市。
3. 程序调用天气函数。
4. 把工具结果交给模型生成最终回答。

## 五、参考答案

### 选择题答案

1. B
2. C
3. A
4. C
5. B
6. B
7. A
8. C
9. B
10. A

### 填空题答案

1. 创建客户端；解析结果
2. 对话消息
3. 云端模型
4. `for`
5. 换行
6. 示例
7. 示例
8. 思维链
9. 投票
10. 观察

### 简答题答案

1. 因为真实项目需要程序自动调用模型、自动处理用户输入、自动解析模型结果，并把结果展示、保存或交给后续流程处理。网页聊天适合体验模型能力，但不适合做自动化业务系统。

2. 批处理是模型生成完整答案后一次性返回，适合短回答和后台任务；流式输出是一段一段返回内容，适合聊天、长文本生成和需要改善用户等待体验的场景。

3. 应先打印完整响应对象，查看真实返回结构，再根据字段层级取值。不要直接猜字段，也不要在换模型后继续照搬旧的解析路径。

4. zero-shot 是不给示例，直接让模型完成任务；few-shot 是给模型少量示例，让模型模仿示例的格式、风格或判断标准。

5. few-shot 只是把示例放进提示词上下文中，让模型临时参考，不会修改模型参数，也不会让模型永久学会这些示例。

6. CoT 适合数学题、逻辑题、多步骤任务、代码分析等复杂推理任务。简单任务不一定适合 CoT，因为它会增加 token 消耗和响应时间。

7. CoT 多数是在一个提示词中要求模型分步推理；链式提示更偏工程实现，是把一个大任务拆成多个子任务，让前一步结果作为下一步输入。

8. Self-Consistency 的优点是提高复杂推理任务的稳定性；代价是需要多次调用模型，会增加 token 成本、运行时间和代码复杂度。

9. 模型负责思考下一步、选择工具、总结工具结果；程序负责提供工具、执行工具、校验工具调用和返回结果。

10. 可以通过分隔符隔离用户输入、明确任务边界、不把敏感信息放入提示词、限制工具调用权限、对输出进行安全检查等方式防御。

## 六、代码题参考答案

### 1. 大模型基础调用

```python
"""
需求：
    使用 OpenAI 兼容接口调用云端大模型，让模型回答一个学习类问题。

步骤：
    1. 导入 OpenAI 类。
    2. 创建客户端对象，配置模型服务地址。
    3. 使用 messages 组织用户问题。
    4. 调用模型并解析回答。
"""

from openai import OpenAI


# 创建客户端对象。
# 客户端可以理解为 Python 程序和模型服务之间的连接入口。
client = OpenAI(
    # 这里使用 DashScope 的 OpenAI 兼容接口。
    # API Key 建议提前配置到环境变量中，不要直接写死在代码里。
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 调用模型生成回答。
response = client.chat.completions.create(
    # 指定模型名称。
    model="qwen-plus",

    # messages 是对话列表。
    # 这里只有一个 user 消息，表示用户真实提问。
    messages=[
        {
            "role": "user",
            "content": "请用三句话说明 Python 程序员为什么要学习大模型 API 调用。"
        }
    ]
)

# 从返回对象中取出模型回答。
# choices[0] 表示取第一条候选结果。
# message.content 表示真正的回答文本。
answer = response.choices[0].message.content

# 打印回答，方便在控制台查看。
print(answer)
```

### 2. 流式输出

```python
"""
需求：
    使用流式输出，让模型回答内容逐段显示，模拟聊天软件的打字效果。

步骤：
    1. 创建模型客户端。
    2. 调用模型时设置 stream=True。
    3. 使用 for 循环读取每个返回片段。
    4. 连续打印每个片段。
"""

from openai import OpenAI


client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 开启 stream=True 后，返回值不再是完整回答对象，
# 而是一个可以逐段读取的流式对象。
stream = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {
            "role": "user",
            "content": "请用通俗语言解释什么是大模型流式输出。"
        }
    ],
    stream=True
)

# 遍历流式对象。
# chunk 表示模型本次返回的一小段内容。
for chunk in stream:
    # delta.content 是当前新增的文本片段。
    content = chunk.choices[0].delta.content

    # 有些片段可能为空，所以先判断再打印。
    if content:
        # end=""：不自动换行，让文本连续显示。
        # flush=True：立即刷新，让学生看到实时输出效果。
        print(content, end="", flush=True)
```

### 3. Few-shot 翻译

```python
"""
需求：
    使用 few-shot 提示词，让模型参考一个翻译示例，再翻译新的英文句子。

步骤：
    1. 在 system 消息中写清楚模型角色和示例。
    2. 在 user 消息中放入真正要翻译的句子。
    3. 调用模型并打印翻译结果。
"""

from openai import OpenAI


client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# system_prompt 中包含角色、要求和示例。
# 这个示例不会训练模型，只是让模型临时模仿格式。
system_prompt = """
你是一个英文到中文的翻译助手。
请参考下面的示例进行翻译，只输出中文结果，不要输出多余解释。

示例：
英文：I love Python.
中文：我喜欢 Python。
"""

response = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Large models can call external tools."}
    ]
)

print(response.choices[0].message.content)
```

### 4. Zero-shot CoT

```python
"""
需求：
    使用 Zero-shot CoT，让模型面对复杂年龄题时一步一步推理。

步骤：
    1. 构造题目。
    2. 在提示词中加入“请一步一步思考”。
    3. 调用模型并打印推理过程和答案。
"""

from openai import OpenAI


client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

question = """
当小明 6 岁时，他的妹妹年龄是他的一半。他的哥哥比小明大 4 岁。
现在小明 70 岁了，请问他的妹妹和哥哥年龄加起来是多少？
"""

prompt = f"""
请解决下面的问题。

题目：
{question}

要求：
1. 请一步一步思考。
2. 先写出推理过程。
3. 最后单独给出最终答案。
"""

response = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)
```

### 5. 链式提示

```python
"""
需求：
    使用链式提示完成“抽取要点 -> 生成摘要 -> 优化摘要”的三步任务。

步骤：
    1. 第一次调用模型：从原文中抽取要点。
    2. 第二次调用模型：根据要点生成摘要。
    3. 第三次调用模型：优化摘要语言。
    4. 每一步结果都打印出来，方便检查中间过程。
"""

from openai import OpenAI


client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


def ask_model(prompt):
    """
    封装模型调用函数。

    为什么要封装：
        三步链式任务都需要调用模型，如果每次都重复写完整调用代码，会很乱。
        封装以后，只需要传入不同 prompt，就能得到模型回答。

    参数：
        prompt：本次要发送给模型的提示词。

    返回：
        模型生成的文本结果。
    """
    response = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


article = """
近年来，大模型在客服、教育、办公和数据分析等场景中应用越来越广。
企业在使用大模型时，通常需要通过 Prompt 工程约束模型输出格式，
并结合知识库、外部工具和安全审核来提高回答可靠性。
"""

# 第一步：抽取要点。
prompt_1 = f"""
请从下面文本中抽取 3 个关键要点。

文本：
\"\"\"{article}\"\"\"
"""
points = ask_model(prompt_1)
print("第一步：抽取要点")
print(points)
print("-" * 40)

# 第二步：根据要点生成摘要。
prompt_2 = f"""
请根据下面的要点，生成一段 100 字以内的摘要。

要点：
\"\"\"{points}\"\"\"
"""
summary = ask_model(prompt_2)
print("第二步：生成摘要")
print(summary)
print("-" * 40)

# 第三步：优化摘要语言。
prompt_3 = f"""
请优化下面这段摘要，使语言更简洁、正式、适合放在课程笔记中。

摘要：
\"\"\"{summary}\"\"\"
"""
final_summary = ask_model(prompt_3)
print("第三步：优化摘要")
print(final_summary)
```

### 6. Self-Consistency 简化实现

```python
"""
需求：
    使用 Self-Consistency 思路，让模型从多个思路中选择更合理的答案。

步骤：
    1. 让模型生成 3 个不同思路。
    2. 让模型分别按照这些思路回答问题。
    3. 再让模型对多个答案进行评审，选出最终答案。

重要说明：
    不建议使用 eval() 解析模型返回内容。
    eval() 会把字符串当 Python 代码执行，如果字符串中包含恶意代码，会有安全风险。
    更安全的做法是要求模型输出 JSON，然后使用 json.loads() 解析。
"""

import json
from openai import OpenAI


client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


def ask_model(prompt):
    """
    调用模型并返回文本结果。
    这里封装函数，是为了让后续多次调用更清晰。
    """
    response = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


question = "当小明 6 岁时，妹妹 3 岁。现在小明 70 岁，妹妹多少岁？"

# 第一步：要求模型输出 JSON 数组，方便程序解析。
prompt_1 = f"""
请针对下面问题，给出 3 个不同的解题思路。

问题：
{question}

输出要求：
1. 只输出 JSON 数组。
2. 数组中每个元素是一条思路字符串。
3. 不要输出 Markdown，不要输出解释文字。

示例格式：
["思路1", "思路2", "思路3"]
"""

idea_text = ask_model(prompt_1)
print("模型返回的思路 JSON：")
print(idea_text)

# 使用 json.loads 解析 JSON 字符串。
# 如果模型没有严格输出 JSON，这里可能报错，真实项目中应增加异常处理和重试。
ideas = json.loads(idea_text)

answers = []

# 第二步：按照每个思路分别回答。
for idea in ideas:
    prompt_2 = f"""
请按照下面的思路解决问题。

问题：
{question}

思路：
{idea}

要求：
1. 写出简短推理过程。
2. 最后给出答案。
"""
    answer = ask_model(prompt_2)
    answers.append(answer)

print("多个思路得到的答案：")
for item in answers:
    print(item)
    print("-" * 30)

# 第三步：让模型评审多个答案，选出最合理的结果。
prompt_3 = f"""
你是一个严谨的评审员。
请从下面多个答案中选出最合理的答案，并说明理由。

原问题：
{question}

候选答案：
{answers}
"""

final_answer = ask_model(prompt_3)
print("最终评审结果：")
print(final_answer)
```

### 7. ReAct 简化工具调用

```python
"""
需求：
    实现一个简化版 ReAct 天气查询流程。

步骤：
    1. 定义一个天气查询工具 get_weather(city)。
    2. 让模型根据用户问题判断需要查询的城市。
    3. 程序调用工具函数获取天气结果。
    4. 把工具结果交给模型，让模型生成自然语言回答。

注意：
    这里的天气函数是模拟工具，不是真实天气接口。
    重点是理解 ReAct 的分工：
        模型负责判断要查什么。
        程序负责真正执行工具。
"""

from openai import OpenAI


client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


def get_weather(city):
    """
    模拟天气查询工具。

    参数：
        city：城市名称。

    返回：
        该城市的模拟天气结果。

    为什么用函数：
        在真实项目中，这里可以替换成天气 API、数据库查询或其他业务接口。
    """
    weather_data = {
        "深圳": "小雨，25-29℃，湿度较高，建议带伞。",
        "北京": "晴，18-27℃，空气较干燥，适合出行。",
        "上海": "多云，22-28℃，体感舒适。"
    }

    return weather_data.get(city, "暂时没有查询到该城市的天气。")


def ask_model(prompt):
    """
    封装模型调用。
    """
    response = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


user_question = "我明天去深圳上课，需要带伞吗？"

# 第一步：让模型判断需要查询哪个城市。
# 这里要求只输出城市名，是为了方便程序继续处理。
extract_city_prompt = f"""
请从用户问题中提取需要查询天气的城市名。

用户问题：
{user_question}

输出要求：
只输出城市名，不要输出其他解释。
"""

city = ask_model(extract_city_prompt).strip()
print("模型判断需要查询的城市：", city)

# 第二步：程序执行工具。
# 模型不会真的查天气，真正查天气的是 Python 函数。
tool_result = get_weather(city)
print("工具返回结果：", tool_result)

# 第三步：把工具结果交给模型生成最终回答。
final_prompt = f"""
用户问题：
{user_question}

天气工具返回结果：
{tool_result}

请根据工具结果，用自然、简短的语言回答用户。
"""

final_answer = ask_model(final_prompt)
print("最终回答：")
print(final_answer)
```

