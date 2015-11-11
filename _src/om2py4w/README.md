# OMOOC.py 周任务代码试作

## 4w

### 网页版My Dear Diary
#### bottle安装
按照[bottle官网](http://www.bottlepy.org)的命令安装了bottle，并运行了“Hello World”的示例代码：
```
from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)'
```
route()命令将下面的代码执行绑定给了http://localhost:8080/hello/world 这个URL地址。

bottle内置了一个快速强大的模板引擎，称为 SimpleTemplate 模板引擎，可通过 template() 函数或 view()修饰器来渲染一个模板，而只需提供模板的名字和传递给模板的变量。模板的后缀是.tpl

> Bottle comes with a fast and powerful built-in template engine called SimpleTemplate Engine. To render a template you can use the template() function or the view() decorator.
```
@route('/hello')
@route('/hello/<name>')
def hello(name='World'):
    return template('hello_template', name=name)
```
创建一个template，“hello_template.tpl”.

####Start with [Todo-List Application](http://bottlepy.org/docs/dev/tutorial_app.html#tutorial-todo-list-application) 

创建database，连接database都比较容易理解。

创建template： **template**总是返回一系列的字符串，所以不需要再进行格式转换。当我们在写一个template的时候，*以%开始的行都可以被理解为python的代码*。

```
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The open items are as follows:</p>
<table border='1'>
%for row in rows:
	<tr>
	%for col in row:
		<td>{{col}}</td>
	%end
	</tr>
%end
</table>
```
使用for/if/while等时，要记得使用%end来结束它们。如果要访问template里面的一个non-python code，需要使用双花括号，这时也就是告诉template把该变量的真实值插入在这个位置。

**Using POST and GET Values**

request.GET.get() == request.POST.get()

####初步实现Web版Diary####
1. 导入sqlite3，建立diary.db数据库存储日记；
2. 设置网页模板格式；
3. 连接数据库，进行读写操作，并显示在模板中。
运行结果如下图：
![Alt text](./QQ截图20151111191245.png)

测试中文：失败！
把string换成unicode string，
```
 new = new.decode('utf-8')
```
运行结果如下图：
![Alt text](./2222.png)

####如何兼容3w的版本呢？####
目前是使用命令行直接对数据库进行操作。

输入和输出中文又出现问题啦！还在纠结中。。。
