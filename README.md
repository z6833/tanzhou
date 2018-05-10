# tanzhou
一个简单的scrapy使用的小案例
抓取：http://www.tanzhouedu.com/mall/course/initAllCourse
下的所有课程名称和价格，并保存为json格式

网页分析：
是一个ajax加载的页面，每次数据变化，但是url不变化，
通过查看headers中的信息，得到每次点击下一页时真正请求的链接url
观察发现每次翻页，请求变化的是offset的数值和时间戳


1.首先创建一个爬虫项目。
    使用命令：scrapy startproject 'pro_name'  # pro_name是项目名称
    输入命令后，会自动出现一个用pro_name的项目文件夹，
    里面包含一个scrapy项目所必要的文件

2.明确爬取目标，编辑items.py文件，定义需要爬取的字段。

3.编辑爬虫。进入spiders文件夹下，创建爬虫文件。
    使用命令：scrapy genspider 'spider_name' 'start_url'
    生成一个爬虫，名字为spider_name，初始爬取url为start_url
    会在spiders文件夹下生成一个spider_name.py的文件，
    里面包含一个name=‘spider_name’， name是不同爬虫的唯一标识，不能重复
    start_url是爬虫的第一个爬取链接（可修改），并返回一个response
    解析response中的其他可用链接和数据

4.将爬取到的数据通过yield，丢给pipelines.py文件保存，
在pipelines.py文件中编写保存文件的逻辑

5.运行爬虫，使用命令：scrapy crawl "spider_name"

注：在配置文件中打开头信息和管道
