import time
import typing

"""
cache_args save args function in keys and result function, start time in value
cache_args = {
(args) : [result_function, start time]
}
"""
cache_args: dict = {}


def cache(timeout: int = 15):
    def cache_decorator(func):

        """
        The wrapper function takes in arguments and returns a cache result
        if args are in the cache_args key and real time - start time < timeout
        Else return result function
        """
        def wrapper(*args):
            if args in cache_args and time.time() - cache_args[args][0] < timeout:
                cache_args[args][0] = time.time()
                return print(f"result cache: {cache_args[args][1]} {cache_args[args][0]} ")
            else:
                result_func = func(*args)
                cache_args[args] = [time.time(), result_func]
                return print(f"result function: {result_func}")

        return wrapper

    return cache_decorator


@cache(timeout=5)
def calc(a: int, b: int) -> float:
    result = a / b
    return round(result, 2)


try:
    while True:
        arg_func_calc_a = int(input())
        arg_func_calc_b = int(input())
        calc(arg_func_calc_a, arg_func_calc_b)
except Exception as error:
    print(error)
