# DML 增删查改

# 删除以前的数据库
    drop database if exists jd;
# 创建一个新的数据库
    create database jd;
# 使用数据库
    use  jd;
# 查看当前在那个数据库
    select database();

# 查看表列表
SHOW TABLES;

#查看表结构
DESC  stu1;

# 添加表记录
insert into stu1 value (001,'longyou',120.2);

insert into stu1 value (002,'ethan',125.2),(003,'yu',110.2);

insert into stu1(id,name,weight) value (004,'allice',98.2),(005,'peter',178.2);

# 查询具体表数据
select * from stu1;

# 更新表
update stu1 set name='peter',weight=200 where stu1.id=001;

# 删除表数据
delete from stu1 where id=005;

#删除表
delete from db1.stu2






