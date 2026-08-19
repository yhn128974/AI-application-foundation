"""
需求：调用在前面实现的 ”多功能机器人“，实现上传简历文件：素材 **02-简历.docx**到coze平台并实现内容提取
思路步骤：
1. 准备工作：
    1.1 导入必要的模块和类，如json、logging、os、Path、typing及cozepy中的相关类
    1.2 初始化Coze客户端，设置访问令牌和基础URL
    1.3 设定机器人ID和用户ID 
2. 实现文件上传功能：定义upload_file函数，接收文件路径作为参数
3. 上传文件并获取文件ID：
    3.1 指定要上传的文件路径
    3.2 调用upload_file函数上传文件，若上传失败则退出程序
    3.3 获取上传文件的ID
4. 构建多模态消息：构建包含文件的多模态消息
5. 进行流式聊天：
    5.1 调用coze.chat.stream方法创建聊天，传入机器人ID、用户ID、多模态消息列表和参数
    5.2 遍历聊天迭代器，根据不同的ChatEventType进行处理：
        5.2.1 若为CONVERSATION_MESSAGE_DELTA，打印推理内容或正常内容
        5.2.2 若为CONVERSATION_CHAT_COMPLETED，打印token使用情况
        5.2.3 若为CONVERSATION_CHAT_FAILED，打印聊天失败信息
    5.3 捕获聊天过程中的异常并打印错误信息
"""

import json
import logging
import os
from pathlib import Path
from typing import Optional

from cozepy import COZE_CN_BASE_URL, ChatEventType, Coze, DeviceOAuthApp, Message, TokenAuth, \
    MessageObjectString  # noqa

coze_api_token = 'pat_mpFgPO2E0r9lYSxrigiBlx9Q1x38twQytRDIEEz9YMnOVVRdK2pOcDsv8LrciR48'


# 通过access_token初始化Coze客户端
coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=COZE_CN_BASE_URL)

# 在Coze中创建机器人实例，复制网页链接中的最后一个数字作为机器人ID[1](@ref)
bot_id = "7674987338887446582"  # 直接指定机器人ID
# 用户ID用于标识用户身份，开发者可以使用自定义业务ID或随机字符串
user_id = "516118286444264"

parameters = {}  # 直接指定空参数字典



# --- 新增：文件上传功能 ---
def upload_file(file_path: str):
    """
    上传文件到Coze并返回文件信息[1,5](@ref)
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")

        # 检查文件大小（Coze限制为512MB）[5](@ref)
        file_size = os.path.getsize(file_path)
        if file_size > 512 * 1024 * 1024:
            raise ValueError("文件大小超过512MB限制")

        # 使用cozepy的files.upload方法上传文件[1,4](@ref)
        file_response = coze.files.upload(file=Path(file_path))
        print(f"文件上传成功！文件ID: {file_response.id}")
        return file_response
    except Exception as e:
        print(f"文件上传失败: {str(e)}")
        return None


# --- 在调用聊天前，先上传文件 ---
# 指定要上传的文件路径（请替换为您的实际文件路径）
file_to_upload = r'C:\Users\YuEth\Desktop\AI综合学习方案\技术路线\Machine-learning-learning\prompt\work_space\常用提示词框架.md'

# 上传文件
uploaded_file = upload_file(file_to_upload)

if not uploaded_file:
    print("文件上传失败，程序退出。")
    exit(1)

# 获取上传文件的ID，后续消息会用到
file_id = uploaded_file.id

# --- 构建包含文件的多模态消息 ---
# 使用Message.build_user_question_objects构建多模态消息[1](@ref)
# 这里同时支持图片、音频、文本等多种文件类型
additional_messages = [
    Message.build_user_question_objects(
        [
            # 可以同时传入多种类型的文件[1](@ref)
            MessageObjectString.build_file(file_id=file_id),
            # 如果是音频文件，使用：MessageObjectString.build_audio(file_id=file_id)
            # 还可以添加文本描述
        ]
    )
]

# TODO或者使用多模态问答方式，同时包含文本和文件[1](@ref)
# additional_messages = [
#     Message.build_user_multimodal_question(
#         contents=[
#             {"type": "text", "text": "请分析一下这个文件的内容："},
#             {"type": "file", "file_id": file_id}  # 文件部分，使用上传得到的file_id
#         ]
#     )
# ]

print("----- 开始与机器人对话 -----")

# 调用coze.chat.stream方法创建聊天，此方法为流式聊天，返回聊天迭代器
is_first_reasoning_content = True
is_first_content = True

try:
    stream = coze.chat.stream(
        bot_id=bot_id,
        user_id=user_id,
        additional_messages=additional_messages,
        parameters=parameters,
    )

    print("日志ID:", stream.response.logid)

    for event in stream:
        if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
            if event.message.reasoning_content:
                if is_first_reasoning_content:
                    is_first_reasoning_content = not is_first_reasoning_content
                    print("----- 推理内容开始 -----\n> ", end="", flush=True)
                print(event.message.reasoning_content, end="", flush=True)
            else:
                if is_first_content and not is_first_reasoning_content:
                    is_first_content = not is_first_content
                    print("----- 推理内容结束 -----")
                print(event.message.content, end="", flush=True)

        if event.event == ChatEventType.CONVERSATION_CHAT_COMPLETED:
            print()
            print("token使用情况:", event.chat.usage.token_count)
            break

        if event.event == ChatEventType.CONVERSATION_CHAT_FAILED:
            print()
            print("聊天失败", event.chat.last_error)
            break

except Exception as e:
    print(f"聊天过程发生错误: {str(e)}")