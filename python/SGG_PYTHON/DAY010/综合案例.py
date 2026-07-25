
from 正则表达式 import is_china_mobile_phone, is_email

class Customer:
    def __init__(self,id,name,age,phone,email):
        self.id=id
        self.name=name
        self.age=age
        self.phone=phone
        self.email=email


customer_LIST=[]



def add_custome():
    id=input("请输入ID")
    for item in customer_LIST:
        if item.id==id:
            print("该ID已经存在")
            return
    name=input("请输入姓名")
    age=input("请输入年龄")

    # 对电话进行正则验证
    phone=input("请输入电话")
    while not is_china_mobile_phone(phone):
        print("电话号码格式不正确，请重新输入。")
        phone = input("请输入电话")

    # 对邮箱进行正则验证
    email = input("请输入邮箱")
    while not is_email(email):
        print("邮箱地址格式不正确，请重新输入。")
        email = input("请输入邮箱")

    customer=Customer(id,name,age,phone,email)
    customer_LIST.append(customer)
    print("添加成功")

def delete_customer():
    id=input("请输入要删除的ID")
    for item in customer_LIST:
        if item.id==id:
            customer_LIST.remove(item)
            print("删除成功")
            return
    print("没有找到该ID")


def modify_customer():
    id=input("请输入要修改的ID")
    for item in customer_LIST:
        if item.id==id:
            item.name=input("请输入姓名")
            item.age=input("请输入年龄")
            # 
            item.phone=input("请输入电话")
            while not is_china_mobile_phone(item.phone):
                print("电话号码格式不正确，请重新输入。")
                item.phone = input("请输入电话")
            # 
            item.email=input("请输入邮箱")
            while not is_email(item.email):
                print("邮箱地址格式不正确，请重新输入。")
                item.email = input("请输入邮箱")
            print("修改成功")
            return
    print("没有找到该ID")


def query_customer():
    id=input("请输入要查询的ID")
    for item in customer_LIST:
        if item.id==id:
            print(f"ID:{item.id},姓名:{item.name},年龄:{item.age},电话:{item.phone},邮箱:{item.email}")
            return
    print("没有找到该ID")


def show_all_customer():
    if not customer_LIST:
        print("没有客户信息")
        return
    for item in customer_LIST:
        print(f"ID:{item.id},姓名:{item.name},年龄:{item.age},电话:{item.phone},邮箱:{item.email}")


def main():
    while True:
        print('------------------------------')
        print("1.添加客户")
        print("2.删除客户")
        print("3.修改客户")
        print("4.查询客户")
        print("5.显示所有客户")
        print("6.退出")
        print('------------------------------')
        choice=input("请输入你的选择=> ")
        if choice=="1":
            add_custome()
        elif choice=="2":
            delete_customer()
        elif choice=="3":
            modify_customer()
        elif choice=="4":
            query_customer()
        elif choice=="5":
            show_all_customer()
        elif choice=="6":
            break
        else:
            print("输入有误，请重新输入")

 #  
if __name__ == '__main__':

    main()




