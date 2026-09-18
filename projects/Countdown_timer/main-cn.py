import time                                               # 导入 time 模块，用于 sleep() 暂停

t = input('请输入秒数：')                                 # input() 等待用户输入，返回值是字符串类型

def countdown(t):                                        # 定义倒计时函数，参数 t 为总秒数
    while t:                                             # t 不为 0 时循环（Python 中 0 为 False，非 0 为 True）
        mins, secs = divmod(t, 60)                       # divmod(125, 60) → (2, 5)，同时返回商（分钟）和余数（秒）
        timer = '{:02d}:{:02d}'.format(mins, secs)       # :02d 表示用 0 填充到 2 位，如 2:5 → "02:05"
        print(timer, end="\r")                           # end="\r" 让光标回到行首，覆盖上一次输出，实现动态刷新
        time.sleep(1)                                    # 暂停 1 秒，sleep(0.5) 可暂停 0.5 秒1
        t -= 1                                           # 秒数减 1，等价于 t = t - 1

    print('计时完成！')                                   # 循环结束后打印完成提示，此处没有 \r 所以正常换行


countdown(int(t))                                        # int() 将字符串转为整数，传入 countdown 启动倒计时