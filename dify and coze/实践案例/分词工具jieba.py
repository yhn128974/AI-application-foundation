"""
需求：使用jieba分词库对中文文本进行分词
思路步骤：
1. 导入jieba分词库
2. 使用jieba分词库对中文文本进行分词
3. 打印分词结果

"""
import jieba

# 中文文本
text = "我爱北京天安门"

res=jieba.lcut(text)
res2=jieba.lcut(text,cut_all=True)
res3=jieba.lcut_for_search(text)
# 
print(res)
print(res2)
print(res3)
