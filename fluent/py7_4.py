from py7_3 import clock

from functools import lru_cache

# 必须像常规函数那样调用 lru_cache。 这一行中有一对括号
# @functools.lru_cache()。 这么做的原因是， lru_cache 可以接受配置参数
@lru_cache(maxsize=128, typed=False)
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__=='__main__':
    print(fibonacci(6))