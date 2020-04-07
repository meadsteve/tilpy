import time

from tilpy import til


def test_list(stop):
    tic = time.perf_counter()
    start = []
    for x in range(0, stop):
        start.append(x)
    return time.perf_counter() - tic


def test_til(stop):
    tic = time.perf_counter()
    start = til(element_type=int)
    answer = start
    for x in range(0, stop):
        answer = answer.append(x)
    return time.perf_counter() - tic


for items in [10, 1_000, 10_000, 1_000_000]:
    list_time = test_list(items)
    til_time = test_til(items)
    print(f"For items: {items}")
    print(f"{list_time} vs {til_time}")
    print(f"{til_time / list_time} times slower")
    print("\n")
