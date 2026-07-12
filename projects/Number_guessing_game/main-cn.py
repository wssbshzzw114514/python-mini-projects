import random

print("数字猜谜游戏")

# 使用 randint 函数生成
# 1 到 9 之间的随机数
number = random.randint(1, 9)

# 用户猜测数字的机会次数
# 或用户输入到输入框中的次数
# 这里机会次数为 5
chances = 0

print("猜一个数字（1 到 9 之间）：")

# While 循环来计算
# 机会次数
while True:

    # 输入一个 1 到 9 之间的数字
    guess = int(input())

    # 将用户输入的数字
    # 与要猜测的数字进行比较
    if guess == number:

        # 如果用户输入的数字
        # 与 randint 函数生成的
        # 数字相同，则使用循环
        # 控制语句 "break"
        # 跳出循环
        print(
            f'恭喜！你用了 {chances} 次机会猜中了数字 {number}！')
        # 使用 f-string 方法打印最终结果；
        break

    # 检查用户输入的数字
    # 是否小于
    # 生成的数字
    elif guess < number:
        print("你猜的数字太小了：猜一个比", guess, "大的数字")

    # 用户输入的数字
    # 大于生成的
    # 数字
    else:
        print("你猜的数字太大了：猜一个比", guess, "小的数字")

    # 将机会次数增加 1
    chances += 1