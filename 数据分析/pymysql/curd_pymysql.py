# form pymysql import *
import pymysql

def main():
    # 创建Connection链接
    conn = connect(host='localhost',port=3306,database='jd',user='debian-sys-maint',password='yGhzr4v17a2CSVli',charset='utf8')
    # 获取cursor对象
    cs1 = conn.cursor()
    count = cs1.execute('insert into good_cates(name) values("硬盘")')
    # 打印受影响的行数
    print(count)

    count = cs1.execute('insert into goods_cates(name) values("光盘")')
    print(count)

    conn.commit()

    # 关闭对象
    cs1.close()
    # 关闭connection对象
    conn.close()


if __name__ == '__main__':
    main()
