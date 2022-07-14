# 如果心情指数大于60，就可以打游戏

# mood_index = float(input('心情指数为：'))
# if mood_index >= 60:
#     print('心情好')
#     print('这里必须使用缩进')
# else:
#     print('心情不好')

# BMI = 体重 / （身高**2）

user_weight = float(input('请输入您的体重（单位：kg）：'))
user_height = float(input('请输入您的身高（单位：m）：'))
user_BMI = user_weight / (user_height ** 2)

print('您的BMI为：' + str(user_BMI))

# 瘦 小于18.8
# 正常 18.5 到 25
# 大于25 到 30 偏胖
# 大于30 肥胖
if user_BMI <= 18.5:
    print('偏瘦')
elif 18.5< user_BMI < 25:
    print('正常')
elif 25 < user_BMI < 30:
    print('偏胖')
else:
    print('肥胖')