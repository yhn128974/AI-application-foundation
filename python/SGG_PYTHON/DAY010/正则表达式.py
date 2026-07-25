import re


phone_pattern = re.compile(r"^(?:\+?86)?1[3-9]\d{9}$")

email_pattern = re.compile(r"^[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}$")


def is_china_mobile_phone(phone_number):
    """判断字符串是否为中国大陆手机号。"""
    return bool(phone_pattern.fullmatch(phone_number))


def is_email(email):
    """判断字符串是否为邮箱地址。"""
    return bool(email_pattern.fullmatch(email))


def contains_chinese(text):
    """判断字符串是否包含中文字符。"""
    return bool(re.search(r"[\u4e00-\u9fa5]", text))

test_numbers = [
    "13812345678",
    "19912345678",
    "+8613812345678",
    "8613812345678",
    "12812345678",
    "1381234567",
    "138123456789",
]

test_emails = [
    "user@example.com",
    "hello.world@qq.com",
    "name+tag@sub.example.cn",
    "user@",
    "user@example",
    "@example.com",  
    "user@example..com",
    "user@.com",
    "user@example.c",
]

test_chinese_strings = [
    "Hello World",
    "你好世界",
    "Python编程",
    "123abc",
    "English中文Mixed",
    "你好",
    "世界",
    "仅英文",
    "仅数字123",
    "中文标点，。",
]

if __name__ == '__main__':
    for number in test_numbers:
        result = "匹配" if is_china_mobile_phone(number) else "不匹配"
        print(f"{number},{result}")

    for email in test_emails:
        result="匹配" if is_email(email) else "不匹配"
        print(f"{email},{result}")

    for text in test_chinese_strings:
        result = "包含中文" if contains_chinese(text) else "不包含中文"
        print(f"'{text}': {result}")
