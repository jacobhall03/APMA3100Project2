import math
from matplotlib import pyplot


def rand(iteration: int = 50) -> float: 
    starting_value = 1_000
    multiplier = 24_693
    increment = 3517
    modulus = math.pow(2,17)

    x = starting_value
    u = 0.0
    for i in range(0, iteration):
        x = (multiplier * x + increment) % modulus
        u = x / modulus
    
    return u

def sb_wait_time(iteration: int = 50) -> float:
    return math.pow((8 * rand(iteration)), 2.0/3)

# rand_times = []
# expected = []
# for i in range(1,501):
#     for j in range(1,4):
#         rand_times.append(sb_wait_time(i+j*2000))

# for i in range(0, 1501):
#     expected.append(  math.pow(8 * (i / 1500), 2.0/3))

# rand_times.sort()
# pyplot.plot(rand_times)
# pyplot.plot(expected)
# pyplot.show()