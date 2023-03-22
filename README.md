# 制冷剂后端

## 配置方式

### 数据库
```mysql
# 创建数据库
CREATE DATABASE `refrigeration` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';
```
### 后端
```shell
# 首先初始化数据库
python manage.py migrate
# 运行后端
python manage.py runserver 0.0.0.0:8000
```
### api接口

- 参数计算
  - url: `http://127.0.0.1:8000/api/v1/calculate/params`
- 制冷剂查询
  - url: `http://127.0.0.1:8000/api/v1/query/params`