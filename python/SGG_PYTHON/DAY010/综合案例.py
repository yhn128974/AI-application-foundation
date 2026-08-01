
from 正则表达式 import is_china_mobile_phone, is_email


class Customer:
    def __init__(self, customer_id, name, age, phone, email):
        self.id = customer_id
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"ID:{self.id},姓名:{self.name},年龄:{self.age},电话:{self.phone},邮箱:{self.email}"


# 用字典存储，以 ID 为键，查找/删除都是 O(1)，且天然保证 ID 不重复
customer_dict = {}


def is_valid_name(name):
    """姓名不能为空。"""
    return bool(name.strip())


def is_valid_age(age):
    """年龄必须是 0~150 的整数。"""
    return age.isdigit() and 0 <= int(age) <= 150


def input_until_valid(prompt, validator, error_msg, default=None):
    """反复读取输入直到通过校验；default 不为 None 时，直接回车表示保留原值。"""
    hint = f"{prompt}（回车保留：{default}）" if default is not None else prompt
    while True:
        value = input(f"{hint}=> ").strip()
        if default is not None and not value:
            return default
        if validator(value):
            return value
        print(error_msg)


def add_customer():
    customer_id = input("请输入ID=> ").strip()
    if customer_id in customer_dict:
        print("该ID已经存在")
        return

    name = input_until_valid("请输入姓名", is_valid_name, "姓名不能为空，请重新输入。")
    age = input_until_valid("请输入年龄", is_valid_age, "年龄必须是0~150的整数，请重新输入。")
    phone = input_until_valid("请输入电话", is_china_mobile_phone, "电话号码格式不正确，请重新输入。")
    email = input_until_valid("请输入邮箱", is_email, "邮箱地址格式不正确，请重新输入。")

    customer_dict[customer_id] = Customer(customer_id, name, age, phone, email)
    print("添加成功")


def delete_customer():
    customer_id = input("请输入要删除的ID=> ").strip()
    if customer_dict.pop(customer_id, None) is None:
        print("没有找到该ID")
        return
    print("删除成功")


def modify_customer():
    customer_id = input("请输入要修改的ID=> ").strip()
    customer = customer_dict.get(customer_id)
    if customer is None:
        print("没有找到该ID")
        return

    print(f"当前信息：{customer}")
    customer.name = input_until_valid(
        "请输入姓名", is_valid_name, "姓名不能为空，请重新输入。", customer.name)
    customer.age = input_until_valid(
        "请输入年龄", is_valid_age, "年龄必须是0~150的整数，请重新输入。", customer.age)
    customer.phone = input_until_valid(
        "请输入电话", is_china_mobile_phone, "电话号码格式不正确，请重新输入。", customer.phone)
    customer.email = input_until_valid(
        "请输入邮箱", is_email, "邮箱地址格式不正确，请重新输入。", customer.email)
    print("修改成功")


def query_customer():
    customer_id = input("请输入要查询的ID=> ").strip()
    customer = customer_dict.get(customer_id)
    if customer is None:
        print("没有找到该ID")
        return
    print(customer)


def show_all_customer():
    if not customer_dict:
        print("没有客户信息")
        return
    for customer in customer_dict.values():
        print(customer)


# 菜单项：编号 -> (说明, 处理函数)，退出用 None 表示
MENU = {
    "1": ("添加客户", add_customer),
    "2": ("删除客户", delete_customer),
    "3": ("修改客户", modify_customer),
    "4": ("查询客户", query_customer),
    "5": ("显示所有客户", show_all_customer),
    "6": ("退出", None),
}


def main():
    while True:
        print('------------------------------')
        for key, (label, _) in MENU.items():
            print(f"{key}.{label}")
        print('------------------------------')

        choice = input("请输入你的选择=> ").strip()
        if choice not in MENU:
            print("输入有误，请重新输入")
            continue

        handler = MENU[choice][1]
        if handler is None:
            break
        handler()


if __name__ == '__main__':
    main()
