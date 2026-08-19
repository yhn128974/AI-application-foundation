"""
需求：测试使用Pyhon SDK调用Coze的连通性
思路步骤：

1. 设置令牌和API基础地址
2. 初始化Coze客户端：使用TokenAuth类构建认证对象并传入访问令牌，再将认证对象和API基础地址传入Coze类，建立同步coze客户端
3. 展示所有的工作空间
"""

"""
如何使用个人访问令牌初始化Coze客户端。

首先，你需要访问https://www.coze.cn/open/oauth/pats（对于coze.com环境，访问https://www.coze.com/open/oauth/pats）。

点击添加新令牌。设置好合适的名称、过期时间和权限后，点击“确定”生成你的个人访问令牌。请将其存储在安全的环境中，防止此个人访问令牌泄露。
"""


# 从cozepy库中导入相关类和常量
from cozepy import COZE_CN_BASE_URL, Coze, TokenAuth

# 设置令牌
coze_api_token = 'pat_mpFgPO2E0r9lYSxrigiBlx9Q1x38twQytRDIEEz9YMnOVVRdK2pOcDsv8LrciR48'

# 使用默认的COZE_CN_BASE_URL作为API基础地址
# 默认访问的是api.coze.cn，但如果你需要访问api.coze.com，请使用base_url配置要访问的API端点
coze_api_base = COZE_CN_BASE_URL

# Coze SDK提供了TokenAuth类，用于基于固定的访问令牌构建一个认证类。同时，Coze类允许传入一个认证类来构建一个coze客户端。
# 因此，你可以使用以下代码初始化一个coze客户端，或者一个异步coze客户端

# 使用TokenAuth类构建认证对象，并传入访问令牌，再将认证对象和API基础地址传入Coze类，建立一个同步coze客户端
coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=coze_api_base)

user_id = '516118286444264'
account_id = '516118286444264'

workspaces = coze.workspaces.list(
    user_id=user_id,
    coze_account_id=account_id,
)

for workspace in workspaces:
    # workspaces is an iterator. Traversing workspaces will automatically turn pages and
    # get all workspace results.
    print(workspace.model_dump_json(indent=2))
print("logid", workspaces.response.logid)