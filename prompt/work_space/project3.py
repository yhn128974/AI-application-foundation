# 1 导入必备的工具包
from dotenv import load_dotenv
import openai
import os

# 加载环境变量
load_dotenv()

# 定义分类标签与 Few-Shot 示例
categories = ['新闻报道', '财务报告', '公司公告', '分析师报告']

examples = [
    {
        'content': '今日，股市经历了一轮震荡，受到宏观经济数据和全球贸易紧张局势的影响。投资者密切关注美联储可能的政策调整，以适应市场的不确定性。',
        'category': '新闻报道'
    },
    {
        'content': '本公司年度财务报告显示，去年公司实现了稳步增长的盈利，同时资产负债表呈现强劲的状况。经济环境的稳定和管理层的有效战略执行为公司的健康发展奠定了基础。',
        'category': '财务报告'
    },
    {
        'content': '本公司高兴地宣布成功完成最新一轮并购交易，收购了一家在人工智能领域领先的公司。这一战略举措将有助于扩大我们的业务领域，提高市场竞争力',
        'category': '公司公告'
    },
    {
        'content': '最新的行业分析报告指出，科技公司的创新将成为未来增长的主要推动力。云计算、人工智能和数字化转型被认为是引领行业发展的关键因素，投资者应关注这些趋势',
        'category': '分析师报告'
    }
]

# 待测试预测的数据
sentences = [
    "今日，央行发布公告宣布降低利率，以刺激经济增长。这一降息举措将影响贷款利率，并在未来几个季度内对金融市场产生影响。",
    "ABC公司今日发布公告称，已成功完成对XYZ公司股权的收购交易。本次交易是ABC公司在扩大业务范围、加强市场竞争力方面的重要举措。据悉，此次收购将进一步巩固ABC公司在行业中的地位，并为未来业务发展提供更广阔的发展空间。详情请见公司官方网站公告栏",
    "公司资产负债表显示，公司偿债能力强劲，现金流充足，为未来投资和扩张提供了坚实的财务基础。",
    "最新的分析报告指出，可再生能源行业预计将在未来几年经历持续增长，投资者应该关注这一领域的投资机会"
]


# 2 构建函数，进行prompt设计（描述清楚任务及输出格式）
def init_prompts(examples):
    """
    初始化前置prompt，基于 RTCOE 架构，便于模型做 in-context learning。
    """
    system_prompt = (
        "# Role (角色身份)\n"
        "你是一名资深金融风控与文本分析专家，具备深厚的金融知识。\n\n"
        "# Context (背景上下文)\n"
        "你需要处理来自金融资讯平台的短文本数据，准确归类以支持自动风控与舆情监控。\n\n"
        "# Task (核心任务)\n"
        "分析传入的金融文本，精确归类到以下四种预设类别之一：\n"
        "- 新闻报道\n- 财务报告\n- 公司公告\n- 分析师报告\n\n"
        "# Constraints & Rules (规则与约束)\n"
        "1. 兜底逻辑：若文本不属于以上任何一类或语义模糊无法判定，必须且只能返回：'不清楚类型'。\n"
        "2. 输出限制：必须且只能输出最终的类别名称字符串，严禁包含任何标点符号、解释性文字、引导词或 Markdown 标签。\n"
        "3. 防幻觉约束：严格依据文本本身内容判定，严禁主观推测文本未提及的隐藏含义。\n\n"
        "# Output Format (输出格式)\n"
        "新闻报道 | 财务报告 | 公司公告 | 分析师报告 | 不清楚类型"
    )
    pre_history = [{"role": "system", "content": system_prompt}]

    for item in examples:
        content = item['content']
        category = item['category']
        user_msg = f"'{content}' 是 ['新闻报道', '财务报告', '公司公告', '分析师报告'] 里的什么类别？"
        pre_history.append({"role": "user", "content": user_msg})
        pre_history.append({"role": "assistant", "content": category})

    return {'pre_history': pre_history}


# 3 构建推理函数
def model_chat(content: str, history=[]) -> str:
    """
    调用大模型对话接口
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
def clean_response(response: str) -> str:
    """
    清理并校验模型输出，确保返回标准的分类结果
    """
    response_clean = response.strip().strip("'\"`")
    valid_categories = ['新闻报道', '财务报告', '公司公告', '分析师报告']
    for cat in valid_categories:
        if cat in response_clean:
            return cat
    if '不清楚' in response_clean:
        return '不清楚类型'
    return response_clean


# 5 调用推理 + 后处理
if __name__ == '__main__':
    prompts_info = init_prompts(examples)
    for idx, sentence in enumerate(sentences, 1):
        user_prompt = f"'{sentence}' 是 ['新闻报道', '财务报告', '公司公告', '分析师报告'] 里的什么类别？"
        raw_result = model_chat(user_prompt, history=prompts_info['pre_history'])
        final_result = clean_response(raw_result)
        print(f"sentence {idx}-->{sentence}")
        print(f"result-->{final_result}\n")
