from collections import deque  # allow print deque


def plus_one_second(clock):  # [hh,mm,ss+1]
    clock[2] += 1
    if clock[2] >= 60:
        clock[2] = 0
        clock[1] += 1
        if clock[1] >= 60:
            clock[0] += 1
            clock[1] = 0
            if clock[0] >= 24:
                clock[0] = 0
    return clock   # [hh,mm,ss]


# input Robots
line = input().split(';')
free_robots = deque()   # [name, processing_time]
busy_robots = deque()   # [name, current_time]
processing_times = {}      # name : processing_time

for i in range(len(line)):
    parts = line[i].split('-')
    free_robots.append([parts[0], int(parts[1])])
    processing_times[parts[0]] = int(parts[1])

# input start_time
start_time = [int(x) for x in input().split(':')]  # [hh,mm,ss]

# input products
products = deque()
while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

while len(products) > 0:
    # product is coming from the line each second
    start_time = plus_one_second(start_time)
    product = products.popleft()

    if len(free_robots) > 0:   # there are free robots
        robot = free_robots.popleft()
        busy_robots.append(robot)

        # log record
        time = f'[{start_time[0]:02d}:{start_time[1]:02d}:{start_time[2]:02d}]'
        print(f'{robot[0]} - {product} {time}')
    else:
        # there is not a free robot
        products.append(product)

    for robot in busy_robots:
        robot[1] -= 1
        if robot[1] <= 0:
            time = processing_times[robot[0]]
            name = robot[0]
            free_robot = [name, time]
            free_robots.append(free_robot)
    busy_robots = [robot for robot in busy_robots if robot[1] > 0]
