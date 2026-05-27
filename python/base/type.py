numer1: int = 100
string1: str = 'hello'
flage: bool = True
pic: None = None

list1: list[str|int] = ['a', 'b', 'c']
setlist: set[str] = {'a', 'b', 'c'}
options: dict[str, int] = {
    'a': 1,
    'b': 2,
}
list2: tuple[str, int, int] = ('hello', 1, 2)

#
list1.append(100)

# 函数指定类型
def calc(scores:list[float])->float:
    return sum(scores) / len(scores)
print(calc([1,2,3,4]))

def calc(scores:list[float])->tuple[float, float,float]:
    max_value = max(scores)
    min_value = min(scores)
    avg = sum(scores) / len(scores)
    return max_value, min_value, avg
print(calc([1,2,3,4]))


