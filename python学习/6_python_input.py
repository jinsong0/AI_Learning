# input()一律返回字符串类型
user_age = int(input("请输入您的年龄："))
user_age_after_10_years = user_age + 10
# print("您十年后会是" + user_age_after_10_years + "岁")
print("您十年后会是" + str(user_age_after_10_years) + "岁")

print("\n")
# S = int(input("要不试试会不会报错吧"))
# print(S)


# BMI = weight / (height ** 2)
user_weight = input("请输入您的体重(kg)：")
user_height = input("请输入您的身高(m)：")
User_BMI = float(user_weight) / (float(user_height) ** 2)
print(f'您的BMI指数为：{User_BMI}')
if User_BMI < 18.5:
    print("您的体重过轻")
elif User_BMI < 25:
    print("您的体重正常")
elif User_BMI < 30:
    print("您的体重过重")
else:
    print("您的体重肥胖")

