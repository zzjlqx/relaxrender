# Pytest
[csdn blog](https://blog.csdn.net/liuchunming033/article/details/46501653)

pytest是python的一种单元测试框架
与python自带的unittest测试框架类似，但是比unittest框架使用起来更简洁，效率更高
它具有如下特点：
- 非常容易上手，入门简单，文档丰富，文档中有很多实例可以参考
- 能够支持简单的单元测试和复杂的功能测试
- 支持参数化
- 执行测试过程中可以将某些测试跳过，或者对某些预期失败的case标记成失败
- 支持重复执行失败的case
- 支持运行由nose, unittest编写的测试case
- 具有很多第三方插件，并且可以自定义扩展
- 方便的和持续集成工具集成

## example 

(放到空目录下)
>test_sample.py
```py
def func(x):  
    return x+1  
  
def test():  
    assert func(3) == 5  

def test2():  
    assert func(3) == 6

def test_adaasd():  
    assert func(3) == 4  

class Testo0Old:
        def test_one(self):
            x='this'
            assert 'h' in x
```
> pytest

会出现 2 failed,2 passed 的结果
pytest 自动在当前目录下,寻找所有以test开头或结尾的py文件,并在找到测试文件中寻找以test开头的测试函数或以Test(以上两个均区分大小写)开头的类,并执行

我们编写测试类不能带有__init__方法x