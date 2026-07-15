import random

print("猜数字游戏")

number = random.randint(1, 9)   # 使用 randint 函数生成，1 到 9 之间的随机数
# 用户猜测数字的机会次数
# 或用户输入到输入框中的次数
# 这里机会次数为 5，原始值为1，第一次游戏不消耗次数
chances = 1

print("猜一个数字（1 到 9 之间，您有五次机会）：")

# While 循环来计算机会次数
while chances <= 5:
    guess = int(input())    # 输入一个 1 到 9 之间的数字
    if guess in range(1,10):     # 检查用户输入的数字是否在1-9范围内

        if guess == number:
            print(f'恭喜！你用了 {chances} 次机会猜中了数字 {number}！')
            break
        elif guess < number:
            print(f"你猜的数字太小了：猜一个比{guess}大的数字，您还剩下{5 - chances}次机会")
            chances += 1    #次数+1
        elif guess > number:
            print(f"你猜的数字太大了：猜一个比{guess} 小的数字，您还剩下{5 - chances}次机会")
            chances += 1    # 次数+1

    else:
        print("请输入1-9以内的数字，本次不消耗次数")
else:
    print("您的五次机会用完了，游戏结束")

