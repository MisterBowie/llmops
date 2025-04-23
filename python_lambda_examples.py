"""
Python Lambda函数 - 综合示例

Lambda函数（也称为匿名函数）是小型的、单行的函数，
它们不需要正式的def语句和名称。它们使用'lambda'关键字定义。

基本语法: lambda 参数: 表达式

主要特点:
- 只能包含单个表达式（不能包含语句）
- 可以接受任意数量的参数
- 返回表达式的值
- 可以在任何需要函数对象的地方使用
"""

print("=" * 50)
print("基础LAMBDA示例")
print("=" * 50)

# 示例1: 简单的加法lambda函数
add = lambda x, y: x + y
print(f"示例1: add(5, 3) = {add(5, 3)}")  # 输出: 8

# 示例2: 计算平方的lambda函数
square = lambda x: x ** 2
print(f"示例2: square(4) = {square(4)}")  # 输出: 16

# 示例3: 没有参数的lambda函数
greeting = lambda: "你好，世界！"
print(f"示例3: greeting() = {greeting()}")  # 输出: 你好，世界！

# 示例4: 带条件表达式的lambda函数（三元运算符）
is_even = lambda x: "偶数" if x % 2 == 0 else "奇数"
print(f"示例4: is_even(4) = {is_even(4)}")  # 输出: 偶数
print(f"示例4: is_even(5) = {is_even(5)}")  # 输出: 奇数

print("\n" + "=" * 50)
print("LAMBDA与内置函数一起使用")
print("=" * 50)

# 示例5: 将lambda与map()函数一起使用
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"示例5: map(lambda x: x**2, {numbers}) = {squared_numbers}")
# 输出: [1, 4, 9, 16, 25]

# 示例6: 将lambda与filter()函数一起使用
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"示例6: filter(lambda x: x % 2 == 0, {numbers}) = {even_numbers}")
# 输出: [2, 4]

# 示例7: 将lambda与sorted()函数一起使用
students = [
    {'name': '小丽', 'age': 25},
    {'name': '小明', 'age': 20},
    {'name': '小华', 'age': 22}
]
sorted_students = sorted(students, key=lambda student: student['age'])
print(f"示例7: 按年龄排序学生:")
for student in sorted_students:
    print(f"  {student['name']}: {student['age']}岁")
# 输出: 小明: 20岁, 小华: 22岁, 小丽: 25岁

# 示例8: 将lambda与reduce()函数一起使用
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"示例8: reduce(lambda x, y: x * y, {numbers}) = {product}")
# 输出: 120 (1*2*3*4*5)

print("\n" + "=" * 50)
print("高级LAMBDA示例")
print("=" * 50)

# 示例9: 带多个参数的lambda函数
calculate = lambda x, y, operation: operation(x, y)
add_op = lambda x, y: x + y
multiply_op = lambda x, y: x * y

print(f"示例9: calculate(5, 3, add_op) = {calculate(5, 3, add_op)}")  # 输出: 8
print(f"示例9: calculate(5, 3, multiply_op) = {calculate(5, 3, multiply_op)}")  # 输出: 15
print(f"示例9: calculate(5, 3, lambda x, y: x - y) = {calculate(5, 3, lambda x, y: x - y)}")  # 输出: 2

# 示例10: 返回lambda的函数（闭包）
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)

print(f"示例10: double(5) = {double(5)}")  # 输出: 10
print(f"示例10: triple(5) = {triple(5)}")  # 输出: 15

# 示例11: 列表推导式中的lambda函数
operations = [(lambda x: x + 1), (lambda x: x * 2), (lambda x: x ** 2)]
value = 5
results = [op(value) for op in operations]
print(f"示例11: 对{value}应用多个操作: {results}")
# 输出: [6, 10, 25]

# 示例12: 带默认参数的lambda函数
greet = lambda name, greeting="你好": f"{greeting}, {name}!"
print(f"示例12: greet('小丽') = {greet('小丽')}")  # 输出: 你好, 小丽!
print(f"示例12: greet('小明', '嗨') = {greet('小明', '嗨')}")  # 输出: 嗨, 小明!

print("\n" + "=" * 50)
print("实际应用场景")
print("=" * 50)

# 示例13: 数据转换
data = [{'name': '苹果', 'price': 10.0},
        {'name': '香蕉', 'price': 5.0},
        {'name': '橙子', 'price': 8.0}]

# 只提取名称
names = list(map(lambda item: item['name'], data))
print(f"示例13: 提取名称: {names}")
# 输出: ['苹果', '香蕉', '橙子']

# 对所有价格应用折扣
discounted = list(map(lambda item: {**item, 'price': item['price'] * 0.9}, data))
print(f"示例13: 打9折后:")
for item in discounted:
    print(f"  {item['name']}: ¥{item['price']:.2f}")

# 示例14: 使用多个条件的自定义排序
people = [
    {'name': '小丽', 'age': 25, 'height': 165},
    {'name': '小明', 'age': 20, 'height': 180},
    {'name': '小华', 'age': 20, 'height': 175}
]

# 按年龄升序排序，对于相同年龄则按身高降序排序
sorted_people = sorted(people, key=lambda x: (x['age'], -x['height']))
print(f"示例14: 按年龄排序，然后按身高降序排序:")
for person in sorted_people:
    print(f"  {person['name']}: {person['age']}岁, 身高{person['height']}厘米")

# 示例15: 事件处理（模拟）
def button_click(callback):
    event_data = {'x': 100, 'y': 150, 'button': '左键'}
    return callback(event_data)

result = button_click(lambda event: f"在坐标 ({event['x']}, {event['y']}) 处用{event['button']}点击")
print(f"示例15: {result}")

print("\n" + "=" * 50)
print("局限性和最佳实践")
print("=" * 50)

print("Lambda函数的局限性:")
print("1. 只能包含表达式，不能包含语句")
print("2. 限制为单个表达式")
print("3. 复杂操作可能更难阅读")
print("4. 没有文档字符串用于文档")

print("\n最佳实践:")
print("1. 用于简短、简单的操作")
print("2. 对于复杂逻辑使用命名函数")
print("3. 避免对多次重用的函数使用lambda")
print("4. 考虑可读性 - 有时常规函数更清晰")

print("\n何时使用lambda:")
print("1. 与高阶函数如map()、filter()、sorted()一起使用")
print("2. 用于简短的回调函数")
print("3. 当你需要在行内使用简单函数对象时")
print("4. 用于简单的数据转换")

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("运行此文件以查看所有示例的实际效果！")
    print("=" * 50) 