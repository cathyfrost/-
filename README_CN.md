# 新生信息导入工具

[English](https://github.com/cathyfrost/CXY_2024_DATA/blob/main/README.md)|中文

欢迎使用新生信息导入工具！这个工具可以帮助你将自己的个人信息导入到数据库中，具体步骤请按照下方说明操作。

## 下载
请从[最新发行版](https://github.com/cathyfrost/CXY_2024_DATA/releases/latest)下载 `dist` zip压缩包并解压。这是一个打包好的工具，运行时不需要任何环境。

## 参数
```
 -h, --help             显示帮助信息并退出
--id ID                 记录的序列id
--name NAME             记录的姓名
--class_name CLASS_NAME 记录的班级
--college COLLEGE       记录的学院
--political POLITICAL   记录的政治面貌
```

## 使用
你应该使用命令行工具或者批处理文件来添加你的记录，将您的信息作为参数运行程序来发送您的信息给服务器。
```
data.exe --id ID --name NAME --class_name CLASS_NAME --college COLLEGE --political POLITICAL
```
如下内容是个样例：
```
data.exe --id 22030531 --name "小唐" --class_name "23软件一" --college "计算机信息工程学院" --political "共青团员"

```
> # 注意
> id不是字符，college是二级学院不是大学名字。

如果导入顺利，您将会收到“记录插入成功”的反馈
