# DDL语言
# 查看有那些数据库，确认链接
SHOW DATABASES ;

# 创建数据库
CREATE  DATABASE DB1 CHARSET=utf8;
# IF
CREATE DATABASE IF NOT EXISTS DB1 CHARSET=utf8;

# 删除数据库
DROP DATABASE DB1;

#IF DROP
DROP DATABASE IF EXISTS DB1;

# 使用数据库
USE DB1;

# 查看我在那个数据库
SELECT  database();

#创建表
CREATE TABLE stu1(
    id INT PRIMARY KEY ,
    name VARCHAR(100),
    weight FLOAT
);

# IF
CREATE TABLE  IF NOT EXISTS stu2(
     id INT PRIMARY KEY ,
    name VARCHAR(100),
    weight FLOAT
);
# 查看表列表
SHOW TABLES;

#查看具体表结构
DESC  stu1;

# 删除表
DROP TABLE IF EXISTS stu2;















