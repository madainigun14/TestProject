def decorator_with_name(flag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if flag:
                print(f"The function name is: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
 
# 使用 @decorator_with_name 装饰器，传入一个布尔值来决定是否打印函数名
@decorator_with_name(True)
def my_function():
    print("This is my function.")
 
my_function()




##https://blog.csdn.net/qq_44236589/article/details/88956561
import functools
import inspect

def is_admin(fun):
    @functools.wraps(fun)
    def wrapper(*args,**kwargs):
        #inspect.getcallargs返回一个字典，key值是形参，value值
        #是对应的实参{'name':'root'}
        inspect_res = inspect.getcallargs(fun,*args,*kwargs)
        print('inspect的返回值: %s' %inspect_res)
        if inspect_res.get('name') == 'root':
            res = fun(*args,**kwargs)
            return res
        else:
            print('not root user!')
    return wrapper

login_session = ['root', 'redhat', 'westos']

def is_login(fun):
    @functools.wraps(fun)
    def wrapper(*args,**kwargs):
        if args[0] in login_session:
            res = fun(*args,**kwargs)
            return res
        else:
            print('Error:%s未登录' %args[0])
    return wrapper



@is_login
@is_admin
def add_student(name):
    print('添加学生信息...')

add_student('redhat')

结果为：
inspect的返回值: {'name': 'redhat'}
not root user!




def decorator_a(fun):
    print('Get in decorator_a')

    def inner_a(*args, **kwargs):
        print('Get in inner_a')
        res = fun(*args, **kwargs)
        return res

    return inner_a


def decorator_b(fun):
    print('Get in decorator_b')

    def inner_b(*args, **kwargs):
        print('Get in inner_b')
        res = fun(*args, **kwargs)
        return res

    return inner_b


@decorator_a
@decorator_b
def f(x):
    print('Get in f')
    return x * 2
f(2)
结果为：
Get in decorator_b
Get in decorator_a
Get in inner_a
Get in inner_b
Get in f













