from collections import deque

green = int(input())   # seconds -> 1-100
window = int(input())  # seconds -> 0-100
autos = deque()
total_cars_passed = 0
is_crash = False

command = input()
while command != 'END':
    if command != 'green':
        autos.append(command)
    elif command == 'green' and autos:
        time = green
        is_crash = False
        while autos:
            if time <= 0:
                break
            auto = autos.popleft()
            if len(auto) <= time:
                total_cars_passed += 1
                time -= len(auto)
            elif len(auto) <= (time + window):
                total_cars_passed += 1
                break
            else:
                print('A crash happened!')
                print(f'{auto} was hit at {auto[time + window]}.')
                is_crash = True
                break
    if is_crash:
        break
    command = input()
else:
    print('Everyone is safe.')
    print(f'{total_cars_passed} total cars passed the crossroads.')
