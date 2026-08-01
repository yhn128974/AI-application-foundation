
# count

select count(*) from stu1;

select count(id) from stu1;
#
select count(stu1.weight)  as 质量 from stu1 where weight>100;
#max,min,sum,avg
select
    max(stu1.weight) as 最高体重,
    min(stu1.weight) as 最低体重,
    sum(stu1.weight) as 总计,
    avg(stu1.weight) as 平均体重
    from stu1;
#分组函数
select stu1.id,count(*) from stu1 group by id

