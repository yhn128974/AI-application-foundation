select product.category_id,avg(product.price)
from product
group by category_id
having avg(price)>100;


INSERT INTO category(name) VALUES
('手机'),
('电脑配件'),
('办公用品');

-- 向商品表插入 5 条商品数据。
-- 字段顺序是：商品名称、商品价格、库存数量、所属分类 id。
-- category_id 为 1 表示手机，为 2 表示电脑配件，为 3 表示办公用品。
INSERT INTO product(name, price, stock, category_id) VALUES
('iPhone 15', 5999.00, 100, 1),
('机械键盘', 299.00, 50, 2),
('无线鼠标', 99.00, 80, 2),
('笔记本支架', 59.00, 120, 3),
('安卓充电线', 29.90, 200, 1);


select * from product;

UPDATE product SET price = 279.00 WHERE name = '机械键盘';

# 选择出自营的产品之后根据商品进行分组，筛选出均价大于2000的商品
select product.category_id,avg(product.price) from product group by category_id having avg(price)>1000;

# 根据category_id进行分组,显示category_id,与各组平均价格 最后进行筛选
select category_id, avg(price) from product group by category_id having avg(price)<200;

# limit
select * from product limit 0,10;


insert into product value (7,'口红',200,80,3)



