import math
print(math.pi)
print(math.sqrt(25))
print(math.sin(math.pi/4))
print(math.log2(9))
print(math.log10(10000))
print(math.log(4 ))
# 计算 一元二次方程 的根
import math
a = int(input("请输入a:"))
b = int(input("请输入b:"))
c = int(input("请输入c:"))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print("方程无解")
else:
    x1 = (-b + math.sqrt(delta))/(2 * a)
    x2 = (-b - math.sqrt(delta))/(2 * a)
    if x1 != x2:
        print(f"方程有两个实根分别为 x1={x1:.2f}和 x2={x2:.2f}")
    else:
        print(f"方程有且只有一个实根为 x={x1:.2f}")

