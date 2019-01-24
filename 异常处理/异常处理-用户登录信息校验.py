# 用户登录信息校验
# 步骤：
#   1.用户输入用户名和密码进行校验
#       异常：用户名长度
#             用户名智能出现英文和数字
#             密码长度必须是6位且必须位纯数字组成
# 分析：
#   2.信息使用input操作获取
#   3.自定义异常
#   4.提供检测函数，按异常情况进行处理
#   5.执行try-except完成检测
class NameError(Exception):
    pass
class PwdError(Exception):
    pass

def check_login(name,pwd):
    if len(name) < 3 or len(name) > 8:
        raise NameError("用户名错误")
    if len(pwd) != 6:
        raise PwdException("密码设置错误")

name = input("请输入用户名:")
pwd = input("请输入密码:")

try:
    check_login(name,pwd)
except NameError as e:
    print(str(e))
except PwdError as e:
    print(str(e))
else:
    print("正常登录，请使用")
