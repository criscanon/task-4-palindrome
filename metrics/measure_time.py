import time

def measure_time(func, *args, **kwargs):
    """
    Measure the execution time of a function.

    Args:
        func (callable): The function to be measured.
        *args: Variable-length argument list to pass to the function.

    Returns:
        tuple: A tuple containing the result of the function and the execution time in microseconds.
    """

    total_time = 0
    for _ in range (5):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)

    return result, total_time * 1e6 / 5
