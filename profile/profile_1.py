#-*-coding:utf-8-*-

import cProfile

def foo():
    a = 1
    for i in range(10000):
        a += i
    return a

def bar2():
    a = 1
    for i in range(100000):
        a += 1
    return a


def bar():
    a = 1
    for i in range(100000):
        a += i

    a += bar2()
    return a



def main():
    # 生成 profile对象
    pr = cProfile.Profile()

    # 开启调试
    pr.enable()

    # do somethings
    foo()
    bar()

    # 关闭调试
    pr.disable()

    # 输出结果
    pr.print_stats()

if __name__ == '__main__':
    main()