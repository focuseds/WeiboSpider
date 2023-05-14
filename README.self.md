# 自操作手册

## 操作教程

1. 根据关键词搜集微博
   - 参考`README.md`设置`cookie`
   - 参考`README.md`设定关键词，并爬取数据

2. 根据搜集的微博获取用户信息
   - 将生成的微博数据文件路径填到`my_script.py`中的`read_file`函数中
   - 运行`my_script.py`提取该文件中所有`user_id`，并保存到文件
   - 将文件路径填到`weibospider/spiders/user.py`中的`start_requests`函数中
   - 运行`python run_spider.py user`即可获取关键词下全部用户数据