
# DQL查询语句
select * from stu1 where weight<150;

select id,name from stu1 where weight<150;

# 去重
select  distinct weight from stu1;

select  distinct name from stu1;


# 起别名
select name as current_name,id as currnet_id,weight as 重量 from stu1;

# 给表起名别名
select p.* from stu1 as p;

select * from stu1 where weight>100 and weight<200;

select * from stu1 where weight not between 100 and 200;

select * from stu1 where weight in(98.2,200);

# like 模糊查询 字符匹配
select * from stu1 where name like '%p%';

# _站位符
select * from stu1 where name like '_e%';
# 匹配结尾
select * from stu1 where  name like  '%e';

# 匹配空值
select * from stu1 where  name is not null;

# 排序查询,DESC降序，默认升序
select * from stu1 order by weight;
select * from stu1 order by weight DESC;

# 混合排序,先满足条件一，条件一相同在满足条件二
select * from stu1 order by weight,id;









