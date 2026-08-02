import re

longyou='123456longyou123longyou'
# # match
# res1=re.match(pattern="longyou",string=longyou)
# if res1:
#     print(res1.group())
# else:
#     print("not match")

# # search
# res2=re.search(pattern="longyou",string=longyou)
# if res2:
#     print(res2.group())
# else:
#     print("not search")

# # findall
# res3=re.findall(pattern="longyou",string=longyou)
# if res3:
#     print(res3)
# else:
#     print("not findall")

# 匹配单个字符
# res4=re.search(pattern=r"[^喝酒][^抽烟][^打牌]",string="aa2打牌")
# if res4:
#     print(res4.group())
# else:
#     print("not findall")

# # 匹配数字
# res5=re.search(pattern=r"\d",string="aa2打牌")
# if res5:
#     print(res5.group())
# else:
#     print("not findall")

# # 匹配非数字
# res6=re.search(pattern=r"\D",string="aa2打牌")
# if res6:
#     print(res6.group())
# else:
#     print("not findall")

# # 匹配特殊字符
# res7=re.search(pattern=r"\W\W",string="！aa2打牌")
# if res7:
#     print(res7.group())
# else:
#     print("not findall")

    
# # 匹配非特殊字符
# res8=re.search(pattern=r"\w",string="！aa2打牌")
# if res8:
#     print(res8.group())
# else:
#     print("not findall")
    
# # 匹配高富帅
# res9=re.search(pattern=r"[高][富][帅]",string="白富美高富帅")
# if res9:
#     print(res9.group())
# else:
#     print("not findall")


# *任意匹配
res10=re.search(pattern=r"高富帅*",string="白富美高富帅帅帅帅帅")
if res10:
    print(res10.group())
else:
    print("not findall")

    
    
    