# ============================================================
# 示例：用 OpenAI SDK 调用阿里云百炼 Responses API
# 对应补充材料：04_资料/Day01/补充资料/Completions_API与Responses_API对比说明.md
# 整体流程：导入库 → 创建客户端 → 构造 input → 发起请求 → 解析 output 并打印
# ============================================================

# import os：导入 Python 标准库，用于读取环境变量（如 API Key）
import os

# from openai import OpenAI：从 openai 包引入客户端类
# 虽然叫 OpenAI SDK，但通过 base_url 可指向阿里云百炼的兼容接口
from openai import OpenAI

# ------------------------------------------------------------------
# 第 1 步：创建 API 客户端
# 注意：Responses API 使用的 base_url 与 Chat Completions 不同（见补充材料对比表）
# ------------------------------------------------------------------
client = OpenAI(
    # api_key：百炼平台的 API 密钥，从环境变量 DASHSCOPE_API_KEY 读取
    api_key=os.getenv("DASHSCOPE_API_KEY"),

    # base_url：Responses API 的百炼兼容地址（v2 协议）
    # 与 01 号文件的 compatible-mode/v1 不同，这里是 v2/apps/protocols/compatible-mode/v1
    base_url="https://dashscope.aliyuncs.com/api/v2/apps/protocols/compatible-mode/v1",
)

# ------------------------------------------------------------------
# 第 2 步：发起 Responses API 请求
# client.responses.create(...)：OpenAI 新一代「响应式」接口（非 chat.completions）
# ------------------------------------------------------------------
response = client.responses.create(
    # model：指定调用的模型名称
    model="qwen3.7-plus",

    # input：本次请求的输入内容（Responses API 用 input，而非 Completions 的 messages）
    # 可以是简单字符串，也可以扩展为结构化 item 数组（多轮、多模态等场景）
    input="9.9和9.11哪个大？",

    # extra_body：附加到请求体的扩展参数，会原样传给百炼服务端
    extra_body={
        # enable_thinking：是否开启深度思考模式
        # False = 关闭（本示例直接要最终答案）；True = 开启，output 中会出现 reasoning 类型 item
        "enable_thinking": False
    }
)

# ------------------------------------------------------------------
# 第 3 步：解析并打印 response.output 中的各类输出项
# Responses API 的核心特点：一次响应的 output 是「多种类型的 item 列表」，而非单一 message
# ------------------------------------------------------------------
print(response)
# response.output：输出项列表，每个 item 有 type 字段标识类型
# for item in ...：遍历每一个输出项，按 type 分别处理
for item in response.output:

    # item.type == "reasoning"：该 item 是模型的思考/推理过程（需 enable_thinking=True 才会出现）
    if item.type == "reasoning":
        print("【推理过程】")
        # item.summary：推理摘要列表，每项含 text 字段
        for summary in item.summary:
            # summary.text[:500]：只取前 500 个字符，避免控制台输出过长
            print(summary.text[:500])
        print()  # 空行，分隔不同区块

    # item.type == "message"：该 item 是模型的最终正式回复
    elif item.type == "message":
        print("【最终答案】")
        # item.content：正文片段列表；content[0].text 取第一段文本
        print(item.content[0].text)

# 程序结束。若 enable_thinking=True，通常会先打印 reasoning，再打印 message
