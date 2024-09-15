# New Student Information Import Tool

English|[中文](https://github.com/cathyfrost/CXY_2024_DATA/blob/main/README_CN.md)

Welcome to the New Student Information Import Tool! This tool will help you import your personal information into the database, please follow the instructions below.

## Download
Please download the `dist` zip archive from [latest release](https://github.com/cathyfrost/CXY_2024_DATA/releases/latest) and extract it. This is a packaged tool that requires no environment to run.

## Arguments
```
 -h, --help             show help message and exit
--id ID                 ID of the record
--name NAME             Name of the person
--class_name CLASS_NAME Class name of the person
--college COLLEGE       College of the person
--political POLITICAL   Political status of the person
```

## Use
You should use the command line tool or bat file to add records, add your data as args and run the programme to successfully send your data to the server.
```
data.exe --id ID --name NAME --class_name CLASS_NAME --college COLLEGE --political POLITICAL
```
The following is a sample.
```
data.exe --id 22030531 --name "小唐" --class_name "22软件一" --college "计算机信息工程学院" --political "共青团员"
```
> # Attention
> The id is not a character, and college is a second level college not a university name.

If the import is successful, you will receive the message ‘All records inserted successfully’.
