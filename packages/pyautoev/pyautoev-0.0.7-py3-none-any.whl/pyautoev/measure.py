import time

class Result:
    def __init__(self, e):
        self.e = e
def measure_(func, *args, **kwargs):
    """用于测量某个函数的执行时间，并返回结果和耗时的JSON格式"""
    return_result = dict()
    start_time = time.time()
    try:
        result = func(*args, **kwargs)
    except Exception as e:
        # 捕获异常并记录耗时
        end_time = time.time()
        elapsed_time = f"{end_time - start_time:.2f}"
        return_result['result'] = Result(str(e))
        return_result['elapsed_time'] = elapsed_time
    else:
        end_time = time.time()
        elapsed_time = f"{end_time - start_time:.2f}"
        return_result['result'] = result
        return_result['elapsed_time'] = elapsed_time

    return return_result