from collections import deque

bullet_price = int(input())  # 0 - 100
gun_refill = int(input())   # 1 - 5000   # bullets in a magazine of the gun
bullets = deque([int(x) for x in input().split()])   # 1 - 100
locks = deque([int(x) for x in input().split()])   # 1 - 100
intelligence = int(input())

all_bullets = bullets_number = len(bullets)
refill_number = gun_refill

while bullets_number > 0:
    if refill_number == 0:
        refill_number = gun_refill
        print('Reloading!')

    if locks:
        lock = locks.popleft()
        bullet = bullets.pop()
        bullets_number -= 1
        refill_number -= 1
        if bullet <= lock:
            print('Bang!')
        else:
            print('Ping!')
            locks.appendleft(lock)
    else:
        break

if not locks:
    money_earned = intelligence - (all_bullets - bullets_number) * bullet_price
    print(f'{bullets_number} bullets left. Earned ${money_earned}')
else:
    print(f'Couldn\'t get through. Locks left: {len(locks)}')
