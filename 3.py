"""
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
完全平方数:可以表示一个整数平方的正整数
"""
"""
2018-4-16
"""
for num in range(-100,100000):
    num += 100
    num_sqrt = num ** 0.5
    if num_sqrt.is_integer():
        num += 168
        num_sqrt = num ** 0.5
        if num_sqrt.is_integer():
            print(num - 100 - 168)