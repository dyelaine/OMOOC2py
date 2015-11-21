# OMOOC.py 周任务代码试作

## 5w

###Week 5 Paas版本Diary###

####配置本地开发环境####
直接使用 pip 或者 easy_install 安装 sae-python-dev 包即可。
[安装指南](http://www.sinacloud.com/doc/sae/python/tools.html)

根据官方文档中，安装成功后，进入应用的本地开发目录，也就是index.wsgi和config.yaml所在的目录。这里提到的两个文档都需要自行创建。根据[入门指南](http://www.sinacloud.com/doc/sae/python/tutorial.html)，创建index.wsgj文件如下：
```
import sae

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello, world!']

application = sae.create_wsgi_app(app)
```
创建应用配置文件config.yaml，内容如下：
```
name: helloworld
version: 1
```
在命令行输入dev_server.py，显示结果如下：
![Alt text](./1447396737132.png)
**需要配置mysql？**

尝试访问了http://localhost:8080网站，貌似算成功了，那就先不管MySQL了。
![Alt text](./1447639492060.png)


####KVDB####
参考了前面同学的gitbook，顺便学习下KVDB。
KVDB是SAE开发的分布式key-value数据存储服务，用来支持公有云计算平台上的海量key-value存储。
开发可能会涉及到的命令如下：
**class sae.kvdb.Client(debug=0)**
debug 是否输出详细调试、错误信息到日志，默认关闭
**set(key, val, min_compress_len=0)**
设置key的值为val
**get_by_prefix(prefix, limit=100, marker=None)**
从KVDB中查找指定前缀的 key/value pair。返回一个generator，yield的item为一个**(key, value)的tuple**。
参数:	
prefix – 需要查找的key的前缀。
limit – 最多返回的item个数，默认为100。
marker – 指定从哪一个key开始继续查找，只返回该key后面的结果（该key不含在内）。

官方文档的示例中，使用KVDB时需要导入该库，并初始化一个kvdb的对象：
```
import sae.kvdb
kv = sae.kvdb.Client()
```
KVDB默认数据存在内存中，dev_server.py进程结束时，数据会全部丢失，如果需要保存数据， 请使用如下命令行启动dev_server.py。
```
dev_server.py --kvdb-file=kvdb.db
```
####创建temple####
参照week4即可
需要补一下HTML！！！


####代码####
start with：
```
app = Bottle()
application = sae.create_wsgi_app(app)
```
1. 重写week4代码，如何**逆序输出**？？？
```
    r = results[::-1]
```
词典数组的逆序输出done！

2. 如何获取**访问数量**？


####部署应用####
win用户需要先下载svn，下载完运行saecloud deploy没有报错了。

使用git命令将代码

```
$ git init
$ git add .
$ git commit -m "first version"
$ git remote add sae https://git.sinacloud.com/mydeardiary
$ git push sae master:1
```

进入应用发现报错：
![Alt text](./1447903141593.png)

更新版本再次发布后，一直无法解析网页。

在北京c2t2时，在教练的帮助下，发现后来在更新版本时候，一直只是使用了git add 和git push，并没有对新版本代码进行commit，所以其实后期更新的版本其实并没有被push到sae，被自己蠢哭了，很感谢曹教练的耐心帮助！

而且，教练提示：如果出现404报错，一种情况是url服务没有起来，另外一种情况是模板读不进来；基于两种情况，可以在代码中加入一个简单route来进行调试。

git命令还是需要搞明白，git status， git log，git add， git commit， git push

错误原因：git是有本地库和中心库，仅仅add只是把新代码加入了本地库，git commit之后相当于告诉系统本地库的代码区别于中心库，需要更新，这样后面的push才会有效的。否则不commit的话，系统会认为本地库的代码并没有改变，之后的push也就只是提醒你当前的中心库一切都是最新的，并不会执行真正的推送行为。

接下来美化页面需要学习：html，css和boostrap！！！
client端还没有做！