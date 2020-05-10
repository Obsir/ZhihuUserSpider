# ZhihuUserSpider

![](https://img.shields.io/badge/python-3.6%2B-brightgreen)

自动爬取知乎用户的Scrapy爬虫：

* 采用scrapy-redis分布式爬虫框架
* 采用代理池避免IP被封禁而导致爬取失败的问题


代理池实现采用「[ProxyPool](https://github.com/Python3WebSpider/ProxyPool)」配置修改方式请自行参考

### 环境要求

* Python 3.6+
* Redis
* Mongodb
* pymongo
* Scrapy
* scrapy_redis
* requests
* environs
* Flask
* attrs
* retrying
* aiohttp
* loguru
* pyquery
* supervisor
* redis

### 分布式搭建（可选）
修改scrapy.cfg
```shell script
url = http://URL:PORT/ # 服务器URL:Scrapyd端口
```
修改settings.py
```shell script
REDIS_URL = "redis://URL:PORT" # 服务器URL:Redis端口
```

### 修改起点用户
settings.py
```shell script
START_USER = XXX # 知乎url-token
```

### 运行代理池

```shell script
cd ProxyPool
python run.py
```

### 运行爬虫

```shell script
cd zhihuuser
scrapy crawl zhihu
```

### 爬取结果

结果默认保存在本地Mongodb数据库下

### 其他

* 此项目仅限用学习研究，不得用于任何非法商业活动