"""
相较原版的修改：
1：添加计时功能板块，实现正计时
2：倒计时完成后播放音效
"""

import time                                              # 导入 time 模块，用于 sleep() 暂停
import threading

"""倒计时"""
def countdown():                                         # 定义倒计时函数，参数 t 为总秒数
    t = int(input('请输入秒数：'))                         # input() 等待用户输入，返回值是字符串类型
    while t:                                             # t 不为 0 时循环（Python 中 0 为 False，非 0 为 True）
        mins, secs = divmod(t, 60)                       # divmod(125, 60) → (2, 5)，同时返回商（分钟）和余数（秒）
        timer = f'{mins:02d}:{secs:02d}'                 # :02d 表示用 0 填充到 2 位，如 2:5 → "02:05" todo:!!!不熟练 用！！！
        print(f'\r\033[K{timer}', end='', flush=True)    # \r 光标回行首；\033[K 清除行尾旧内容；覆盖刷新 todo:！！！不懂 用！！！
        time.sleep(1)                                    # 暂停 1 秒，sleep(0.5) 可暂停 0.5 秒1
        t -= 1                                           # 秒数减 1，等价于 t = t - 1
    print('\n计时完成！')                                    # 循环结束后打印完成提示，此处没有 \r 所以正常换行

"""正计时"""
def countup():                  # todo：多线程监控键盘输入以开始和停止计时,todo:将计时秒转为时分秒
    t = 0                       # 时间t原始值为0
    runnying = True
    while runnying:
        mins, secs = divmod(t, 60)
        timer = f'{mins:02d}:{secs:02d}'
        time.sleep(1)
        t += 1
        print(f'\r\033[K{timer}', end='', flush=True)                # 刷新输出使时间t

"""主菜单"""
while True:                     # todo：while菜单改为字典菜单
    print(f'主菜单')
    print("输入1：使用倒计时\n"
          "输入2：使用计时\n"
          "输入9：退出程序")

    user_input = input("请输入您要使用的功能")
    if user_input == "1":
        print("二级菜单：倒计时")
        countdown()
        print("继续使用，或者键入9退出程序")
    elif user_input == "2":
        print("二级菜单：正计时")
        countup()
        print("继续使用，或者键入9退出程序")
    elif user_input == "9":
        print("程序结束")
        break
