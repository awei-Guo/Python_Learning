import math
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / 'src'))

# 导入整个 Function 模块，给它起个短别名 fn
from function_learning import Function as fn

# 调用时使用 "fn.函数名" 的格式
print(fn.my_abs(1))
x,y = fn.my_move(1, 1, 3, math.pi/2)
print(x, y)
print(fn.power(3, 3))
print(fn.my_add(0))
a = (2, 3)
print(fn.my_add(*a))

fn.person('郭佳炜', 28, city='Beijing', job='student')
gjw = {'city': 'Beijing', 'job': 'student'}
fn.person_2('郭佳炜', 28, job='student')
fn.person_2('郭佳炜', 28, **gjw)
fn.test('郭佳炜', 18, 23132, city='Beijing', job='student')
test1 = ('gjw', '18', '23123')
test2 = {'city': 'Beijing', 'job': 'student'}
fn.test(*test1, **test2)
print(fn.fact(10))
print(fn.fact_opt(10))


