import math
def my_abs(x):
    if not isinstance(x,(float,int)):
        raise TypeError    #错误处理
    if x>= 0:
        return x
    else:
        return -x

#空函数 还没想好些什么 别的场景也可以用
def nop():
    pass

#二维位置变换 返回双参数
def my_move(x,y,length,angle):
    nx = round(x+length*math.cos(angle),5)
    ny = round(y+length*math.sin(angle),5)    #舍入五位精度
    return nx,ny

#一元二次方程的解
def quadratic(a, b, c):
    if a==0:
        raise ZeroDivisionError
    return (-b-math.sqrt(b**2-4*a*c))/(2*a),(-b+math.sqrt(b**2-4*a*c))/(2*a)

#幂函数
def power(x,n = 2):     #默认参数
    if not isinstance(n,int):
        raise TypeError
    s = 1
    i = 1
    if n == 0:
        return 1
    elif n >= 1:
        while i <= n:
            s *= x
            i += 1
        return s
    else:
        n = abs(n)
        while i <= n:
            s *= x
            i += 1
        return 1/s

#可变参数 函数内部接收的是tuple
def my_add(*args):
    sum1 = 0
    for i in args:
        sum1 += i**2
    return sum1

#关键字参数
def person(name,age,**kw):
    print('name:',name,'age:',age,'others:',kw)

#命名关键字参数 限制关键字参数 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要*了
def person_2(name,age,*,city='Beijing',job):  #*作为分隔符,后面的参数是命名关键字参数
    print('name:', name, 'age:', age, 'city:', city,'job:', job)

#组合参数,顺序必须是必选参数 默认参数 可选参数 命名关键字参数 关键字参数
def test(name,age,*args,city,**kw):
    print('name:', name, 'age:', age, 'args:',args,'city:', city, 'job:', kw)

#递归函数 函数调用是通过栈（stack）这种数据结构实现的,故会出现栈溢出
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
#尾递归优化 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
def fact_opt(n):
    return fact_iter(n, 1)
def fact_iter(num,pro):
    if num == 1:
        return pro
    return fact_iter(num-1,pro*num)

#汉诺塔
def hntow(n,a,b,c):
    if n == 1:
        print(a,' ->',c)
    else:
        hntow(n-1,a,c,b)
        print(a,' ->',c)
        hntow(n-1,b,a,c)

#去除字符串两端的空格
def trim(s):
    if s == ' ':
        return s
    else:
        i=0
        j=len(s)-1
        while i <= j and s[i] == ' ':
            i += 1
        while j >= i and s[j] == ' ':
            j -= 1
    return s[i:j+1]     #切片

#输出key
def output_key(dirc):
    for key in dirc:    #默认输出key
        print(key)
#输出values
def output_values(dirc):
    for values in dirc.values():
        print(values)
#输出key-values(items)
def output_items(my_dict):
    for key,values in my_dict.items():
        print(key,values)
#类似c输出索引和值 str也可以迭代呦
def output_indexm(my_list):
    for index,values in enumerate(my_list):    #enumerate枚举
        print(index,values)

#查找list中的最值
def search_m(my_list):
    if my_list is None or len(my_list) == 0:    #注意区分None和空列表
        return None,None    #不用括号
    else:
        my_min = my_list[0]
        my_max = my_list[0]
        for i in my_list:
            if i > my_max:
                my_max = i
            if i < my_min:
                my_min = i
    return my_min,my_max

#生成式列表[x**2]
def gene_list(n):
    get_list = [x**2 for x in range(1,n+1)]
    return get_list
def gene_evenlist(n):   #生成偶数list
    get_list = [x**2 for x in range(1,n+1) if x % 2 ==0]    #这里的if表示筛选,不能接else
    return get_list
def gene_evenandminus(n):
    return[x ** 2 if x % 2 ==0 else - x for x in range(1,n+1) ]    #这里if else在for前面表示三元条件
def join_str(str1,str2):    #拼接两个str
    return[x + y for x in str1 for y in str2]
#将dict拼接成list
def gene_dtol(my_dict):
    return[k + '=' + v for k,v in my_dict.items()]
#生成器generator
def gene_generator(n):
    return (x for x in range(1,n+1))
#将生成器转换为列表 
def gene_list_from_generator(generator):
    return [x for x in generator]
#generator保存的是算法,不保存结果,如果要输出,需要用到循环(generator是可迭代对象)
def generator_output(generator):
    for i in generator:
        print(i)
#generator函数(函数中有yield关键字,返回的是一个generator
#用generator函数生成斐波那契数列
def fibonbacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b
#杨辉三角
def yhtriangles(n):
    L = [1]
    for i in range(n):
        yield L
        L = [1] + [L[j] + L[j+1] for j in range(len(L)-1)] + [1]

#凡是可作用于next()函数的对象,都是iterator类型,是惰性的
#凡是可作用于for循环的对象,都是iterable类型
#list元素变小写
def lower_list(my_list):
    return[x.lower() if isinstance(x,str) == True else x for x in my_list]    #体会if的位置