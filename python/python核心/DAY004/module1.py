
num1=1

_num2=100

def add_num(num1,num2):
    return num1+num2;

str1="hello World!"
# __all__设置可以限制*方法被导入的成员
__all__=['num1','add_num','str1']

# 防止在被导入时执行，程序会执行两次，被导入时该部分不会被执行，用于模块内的测试代码
if __name__=="__main__":
    print("模块内执行")

print("外部的一个执行程序")