# 嵌套/多条件判断
'''
if [条件一]:
    if [条件二]:
        [语句A]
    else:
        [语句B]
else:
    [语句C]


'''
#若想要语句A执行，首先要满足条件一为真，否则根本不可能执行到里面这个条件二的判断，
#其次它还要满足条件二为真，不然也不会被执行

# mood_index 是用户输入的心情指数，范围是0-100
# 双分支
mood_index = float(input("对象今天的心情指数是："))
if mood_index >= 60:
    print("恭喜，今晚可以打游戏，去吧皮卡丘！")
    print("（づ￣3￣）づ╭❤️～")
else:
    print("不好意思，今晚不能玩，去睡觉吧！")

# 多分支
# mood_index 是用户输入的心情指数，范围是0-100
# is_at_home 为布尔值，表示是否在家
is_at_home = True    #字符串转布尔值怎么转？
mood_index = float(input("对象今天的心情指数是："))
if mood_index < 60:
    if is_at_home:
        print("放弃游戏，低调做人")
    else:
        print("自由！")
else:
    print("恭喜，今晚可以打游戏，去吧皮卡丘！")

