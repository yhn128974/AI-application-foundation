# ============================================================
# 示例：用 OpenAI SDK 调用阿里云百炼（通义千问）大模型
# 整体流程：导入库 → 创建客户端 → 构造消息 → 发起请求 → 流式打印
# ============================================================

# from：Python 的「从…导入…」语法，从指定模块中引入需要的类/函数
# openai：OpenAI 官方 Python 包，提供统一的 chat.completions 调用方式
# OpenAI：包里的客户端类，用来连接大模型 API 并发送请求
from openai import OpenAI

# import os：导入 Python 标准库 os，用于读取操作系统环境变量
import os

# ------------------------------------------------------------------
# 第 1 步：创建 API 客户端（client = 客户端对象，后续所有请求都通过它发起）
# ------------------------------------------------------------------
client = OpenAI(
    # api_key：API 密钥，相当于「账号密码」，服务端凭此识别你的身份并计费
    # os.getenv("DASHSCOPE_API_KEY")：从系统环境变量中读取名为 DASHSCOPE_API_KEY 的值
    # 好处：密钥不写死在代码里，更安全；若未配置环境变量，此处返回 None
    # 备选写法（仅本地调试）：api_key="sk-你的百炼密钥"
    api_key=os.getenv("DASHSCOPE_API_KEY"),

    # # 不要直接把你的key写进代码，安全的方式是用环境变量保存
    # api_key = "123550090124",

    # base_url：API 服务的基础地址（根 URL）
    # 阿里云百炼提供「OpenAI 兼容模式」，所以可以用 OpenAI SDK 直接调用
    # /compatible-mode/v1 表示兼容 OpenAI v1 接口规范
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# ------------------------------------------------------------------
# 第 2 步：构造对话消息（messages = 消息列表，模拟多轮对话）
# ------------------------------------------------------------------
# messages：列表（list），每个元素是一条消息，用字典（dict）表示
# role：角色，常见取值：
#   - "user"     → 用户说的话
#   - "assistant"→ 模型之前的回复（多轮对话时带上，模型才能「记住」上下文）
#   - "system"   → 系统提示词，用来设定模型的人设、规则、输出格式等
# content：该条消息的具体文本内容
messages = [{"role": "user", "content": "你是谁"}]

# ------------------------------------------------------------------
# 第 3 步：发起聊天补全请求（completion = 补全/生成结果）
# client.chat.completions.create(...)：OpenAI SDK 的标准聊天接口
# ------------------------------------------------------------------
completion = client.chat.completions.create(
    # model：指定要调用的模型名称，不同模型能力、价格、速度不同
    model="qwen3.6-flash",

    # messages：传入上面构造好的对话历史，模型会根据这些内容生成回复
    messages=messages,

    # extra_body：额外请求体参数，会原样附加到 HTTP 请求 JSON 中
    # enable_thinking: True → 开启「深度思考」模式，模型会先输出思考过程再给出最终答案
    # 思考内容在流式响应里通过 reasoning_content 字段返回（见下方循环）
    extra_body={"enable_thinking": True},

    # stream=True：开启流式输出（Streaming）
    # True 表示不一次性返回完整结果，而是像打字一样逐块（chunk）推送
    # 好处：用户能更快看到首字，体验更流畅；适合长回复场景
    stream=True
)

# ------------------------------------------------------------------
# 第 4 步：逐块读取流式响应并打印
# ------------------------------------------------------------------

# is_answering：布尔标志（False/True），用来区分当前处于哪个输出阶段
# False → 还在输出「思考过程」；True → 已进入「正式回复」阶段
is_answering = False

# print：向控制台输出文字
# "\n"：换行符； "=" * 20：把 "=" 重复 20 次，用作分隔线，让输出更易读
print("\n" + "=" * 20 + "思考过程" + "=" * 20)

# for chunk in completion：遍历流式返回的每一个数据块
# chunk：单次推送的一小段 JSON 数据，可能只含几个 token（字/词片段）
for chunk in completion:

    # 流式结束时，服务端可能发送一个 choices 为空的 chunk（例如只含 token 用量统计）
    # 若直接访问 chunk.choices[0] 会报 IndexError，因此先判断是否为空
    # not chunk.choices：列表为空时条件为 True
    # continue：跳过本次循环，直接进入下一个 chunk
    if not chunk.choices:
        continue

    # chunk.choices：候选回复列表，通常只有 1 个元素（索引 0）
    # .delta：本次 chunk 相对于上一次的「增量变化」，不是完整内容，而是新增片段
    delta = chunk.choices[0].delta

    # ---------- 处理「思考过程」片段 ----------
    # hasattr(obj, "attr")：检查对象 obj 是否有名为 attr 的属性（防止旧版 SDK 无此字段报错）
    # delta.reasoning_content：深度思考模式下，模型内部推理过程的文本片段
    # is not None：排除字段存在但值为 None 的情况
    if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
        # 只有还没进入正式回复阶段时，才打印思考内容
        if not is_answering:
            # end=""：打印后不自动换行，让多个 chunk 的内容拼接成一行/一段
            # flush=True：立刻刷新输出缓冲区，确保文字实时显示（不等缓冲区满）
            print(delta.reasoning_content, end="", flush=True)

    # ---------- 处理「正式回复」片段 ----------
    # delta.content：模型最终回复正文的增量片段
    # and delta.content：同时排除空字符串，避免打印无意义空内容
    if hasattr(delta, "content") and delta.content:
        # 第一次收到正式回复时，打印分隔标题并切换阶段标志
        if not is_answering:
            print("\n" + "=" * 20 + "完整回复" + "=" * 20)
            is_answering = True  # 标记：此后不再打印思考内容
        print(delta.content, end="", flush=True)

# 循环结束后程序正常退出，无额外代码
