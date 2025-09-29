# 条件语句

# 条件语句语法：
# 如果 条件1 满足:
#     执行 A 行动
# 否则:
#     执行 B 行动


'''
if [条件]:   # 只要求值出来是布尔值也就是True或False, 都可以作为条件
            # 比如： 如果你定义某个变量的值是布尔值，
'''
# 举例：
is_happy = True
if is_happy:
    print("I'm happy today!")
else:
    print("I'm happy today!")

# 比较运算符：
# == 等于
#!= 不等于
# > 大于
# < 小于
# >= 大于等于
# <= 小于等于


# 多条件判断
# BMI = weight / (height ** 2)
user_gender = input("请输入您的性别(男/女)：")
if user_gender == "男":
    print("您好，先生！")
else:
    print("您好，女士！")
user_weight = float(input("请输入您的体重(kg)："))
user_height = float(input("请输入您的身高(m)："))
User_BMI = (user_weight) / ((user_height) ** 2)
print(f'您的BMI指数为：{User_BMI}')
if User_BMI <= 18.5:
    print("此BMI值属于偏瘦范围")
elif 18.5 < User_BMI <= 25:
    print("此BMI值属于正常范围")
elif 25 < User_BMI <= 30:
    print("此BMI值属于偏胖范围")
else:
    print("此BMI值属于肥胖范围")






