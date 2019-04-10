import re


def main():
    email = input("请输入邮箱地址：")
   # 添加转义字符
   ret = re.match(r"[a-zA-Z_0-9]{4,20}@163\.com$", email)
    if ret:
        print("%s符合要求 "% email)
    else:
        print("%s符合要求 "% email)

if __name__ == "__main__":
    main()
