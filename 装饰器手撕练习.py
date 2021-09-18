import time


def test_decorator(func):
    def checkRunningTime():
        print(f"运行前时间: {time.localtime(time.time())}")
        func()
        print(f"运行后时间: {time.localtime(time.time())}")

    return checkRunningTime()


@test_decorator
def a_func():
    print('hello world')


a_func
