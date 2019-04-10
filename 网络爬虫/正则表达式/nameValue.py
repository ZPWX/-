# 判断变量名是否符合要求
import re
def main():
    names = ["age", "_age", "1age", "age1", "age_1_", "age!", "a#123"]
    for name in names:
        # 判断变量名是否符合要求
        # ret = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", name) 
        # 判开头和结尾
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name)
        if ret:
            print("变量名:%s 符合要求" % name)
        else:
            print("变量名：%s 不符合要求 " % name)

if __name__ == "__main__":
    main()
