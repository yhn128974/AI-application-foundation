# 1导入必备的工具包
from dotenv import load_dotenv
import openai
import json
import os

# 加载环境变量
load_dotenv()

# 定义不同实体下的具备属性
schema = {
    '金融': ['日期', '股票名称', '开盘价', '收盘价', '成交量'],
}

IE_PATTERN = "{}\n\n提取上述句子中{}的实体，并按照JSON格式输出，上述句子中不存在的信息用['原文中未提及']来表示，多个值之间用','分隔。"

# 提供一些例子供模型参考
ie_examples = {
    '金融': [
        {
            'content': '2023-01-10，股市震荡。股票古哥-D[EOOE]美股今日开盘价100美元，一度飙升至105美元，随后回落至98美元，最终以102美元收盘，成交量达到520000。',
            'answers': {
                '日期': ['2023-01-10'],
                '股票名称': ['古哥-D[EOOE]美股'],
                '开盘价': ['100美元'],
                '收盘价': ['102美元'],
                '成交量': ['520000'],
            }
        }
    ]
}

sentences = [
    '2023-02-15，寓意吉祥的节日，股票佰笃[BD]美股开盘价10美元，虽然经历了波动，但最终以13美元收盘，成交量微幅增加至460,000，投资者情绪较为平稳。',
    '2023-04-05，市场迎来轻松氛围，股票盘古(0021)开盘价23元，尽管经历了波动，但最终以26美元收盘，成交量缩小至310,000，投资者保持观望态度。',
]


# 2 构建函数，进行prompt设计（描述清楚任务及输出格式）
def build_prompt(ie_examples):
    history_list = [{'role': 'system', 'content': "你是信息提取专家，需要需要完成信息抽取任务。我会给你一个句子，你需要提取句子中的实体，并按照JSON格式输出，如果句子中有不存在的信息用['原文中未提及']来表示，多个值之间用','分隔。"}]

    # 遍历示例，将样本和实体 添加到history_list中
    for type, example_list in ie_examples.items():  # 获取到金融类型
        for example in example_list:  # 遍历每个样本
            sentence = example['content']
            entity_type = '，'.join(schema[type])  # 获取到金融类型需要抽取的实体
            history_list.append({'role': 'user', 'content': IE_PATTERN.format(sentence, entity_type)})
            history_list.append({'role': 'assistant', 'content': json.dumps(example['answers'], ensure_ascii=False)})

    # print(f'history_list-->{history_list}')
    return {'history_list': history_list}


# 3 构建推理函数
def model_chat(content: str, history=[]) -> str:
    """
    调用大模型对话接口
    :param messages: 输入内容
    :param model: 模型名称
    :return: 大模型输出内容 str
    """
    base_url = os.environ.get('DASHSCOPE_BASE_URL') or 'https://ws-tb5h1ovj9i2pokh3.cn-beijing.maas.aliyuncs.com/compatible-mode/v1'
    api_key = os.environ.get('DASHSCOPE_API_KEY') or 'sk-ws-H.ERPLDEY.ZTxv.MEUCIQCF9feg-Kzk6N_L9xxfL6UMaY-uP7iUxz_eeW0zAiZEhQIgKSDN9OjmGpMS2_nVR6Sf5GD3xvAbV1_Z_AeyJ2nJep0'
    model_name = os.environ.get('DASHSCOPE_CHAT_MODEL') or 'qwen3.7-plus'

    client = openai.OpenAI(
        base_url=base_url,
        api_key=api_key
    )
    messages = [{"role": "user", "content": content}]
    response = client.chat.completions.create(
        model=model_name,
        messages=history + messages,
        stream=False,
    )
    text = response.choices[0].message.content
    return text


# 4 构建后处理函数
def clean_response(response: str):
    # 将模型输出进行清理, 将 ```json清理掉
    if '```json' in response:
        response = response.split('```json')[1].split('```')[0]
        # print('response-->', response)
        # 将这个json字符串转为字典
        try:
            return json.loads(response)  # 防止这步转换出错，使用try except
        except:
            return response
    return response


# 5 调用推理+后处理
prompt_dict = build_prompt(ie_examples)
for sentence in sentences:
    print(f'sentence-->{sentence}')
    result = model_chat(sentence, prompt_dict['history_list'])
    final_result = clean_response(result)
    print(f'final_result-->{final_result}')