import mysql.connector
import argparse

# 设置命令行参数解析
parser = argparse.ArgumentParser(description='Insert data into the database.')
parser.add_argument('--id', required=True, help='ID of the record')
parser.add_argument('--name', required=True, help='Name of the person')
parser.add_argument('--class_name', required=True, help='Class name of the person')
parser.add_argument('--college', required=True, help='College of the person')
parser.add_argument('--political', required=True, help='Political status of the person')

args = parser.parse_args()

# 数据库连接
conn = mysql.connector.connect(
    host='****',
    user='****',
    password='****',
    database='****'
)

cursor = conn.cursor()

# 准备插入数据
sql = "INSERT INTO **** (id, name, class_name, college, political) VALUES (%s, %s, %s, %s, %s)"
cursor.execute(sql, (args.id, args.name, args.class_name, args.college, args.political))

# 提交更改
conn.commit()

print("记录插入成功")

# 关闭数据库连接
cursor.close()
conn.close()
