
#转义字符\ 制表符\t
print('\\\t\\!')
print(r'\\\t\\!')    #默认不转义 r''
print(3e100)

#输出多行''' '''
print('''你好!
第一行
第二行''')

print(r'''你好! \n
第一行
第二行''')

#Bull值
print(3 > 2 and 4 > 6)
print(3 > 2 or 4 > 6)
print(not 3 > 2)

#赋值号=的指针特性
a = 'abc'
b = a
a = 'DEF'
print(b)

#除法输出浮点数
print(9/3)
print(10//3)    #地板除 //
print(10%3)    #求余数 %

#python是Unicode编码(2byte)
chr(65535)
ord('你')
'\u4e2d'

#encode编码,decode解码
'ABC'.encode('ascii')
'ABC'.encode('UTF-8')
'中'.encode('UTF-8')    #\x表示不能用ascii表示的字符
b'\xe4\xb8\xad'.decode('UTF-8')
b'\xe4\xb8\xad\xdd'.decode('UTF-8', errors='ignore')
len('A')
len('\x5f\x6a\xf4')
len('中')    #str使用unicode编码,此时len计算字符数
len('中'.encode('UTF-8'))    #转为UTF-8之后,计算字节数

#格式化
print('hello,%s,你存款还有%05d,今年利率%.2f%%' %('郭佳炜',1999,3.21))
print('{0}你好!你存款还剩{1:.1f}'.format('小明',100))
r=15
s=3.14*(r**2)
print(f'半径是{r},面积是{s:.1f}')

#列表list
c = ['郭佳炜','辜仲宣',3]
d = ['你','我','他',c]    #嵌入,依旧指向c
f = [1] + c    #拼接,指向新的内存块
d.append('它')   #在末尾插入
d.insert(1,'true')    #插入
c.pop(2)    #弹出
len(c)
print(c,d,f)

#元组tuple 指向永远不变
t = (1,)  #t=(1) python把()识别为数学符号,所以此时t是整型
m = (c,5,6)
m[0][1]=3
print(m)    #tuple里的list可变

#条件判断
s = int(input('birth:'))
if s >= 18:
    print('adult')
elif s >= 12:
    print('teenager')
else:
    print('young')

#match匹配
h = int(input( 'age:' ))
match h:
    case x if x < 12:
        print('儿童')
    case 13|14|15|16|17|18:
        print('青少年')
    case _:
        print('成年人')

args = ['python','hello.py','data.py']
match args:
    case ['python']:
        print('未指定文件')
    case ['python',file1,*files]:
        print('python运行了:' + file1 + ', ' + ','.join(files))
    case [clean]:
        print('clean')
    case _:
        print('error')

#for in 循环
sum = 0
numbers = list(range(101))  #range()生成的是range对象
for number in numbers:    #用number遍历numbers
    sum += number
print(sum)

#while 循环
sum2 = 0
n = 99
while n > 0:
    sum2 += n
    n -= 2
print(sum2)

#break提前结束循环
n = 1
while n < 100:
    print(n)
    n += 1
    if( n % 15 == 0 ):
        break
print('end')

#continue直接进入下一轮循环,不跳出
n2 = 0
while n2 < 10:
    n2 += 1
    if n2 % 2 == 0:
        continue
    print(n2)

#字典dict list不可作为dict的key
dic = {'郭佳炜':'帅','崔新建':'胖','加宇航':2}
print(dic['郭佳炜'])
print(dic.get('尹卓宇',1) )   #'尹卓宇' in dic
dic.pop('郭佳炜')
print(dic)

#set是没有value,只有key的dict
l = [1,2,2,3,3]
s = set(l)
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)
s1 = {2,3,6}
print(s1 & s)
print(s1 | s)
print(s1 ^ s)

#对于不可变对象str等
a = '郭佳炜'
b = a.replace('郭','')    #a指针不变,b指向新生成的str
print(b,a)
#对于可变对象list等
l = ['郭佳炜','鲤鱼']
b = l.pop(1)
print(b,l)      #l变了
