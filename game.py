import random
def 玩猜数字():                    
    secret = random.randint(1, 100)
    count = 0
    while True:
        guess = int(input("猜一个 1~100 的数字："))
        count = count + 1
        if guess > secret:
            print("大了")
        elif guess < secret:
            print("小了")
        else:
            print(f"恭喜你！猜了 {count} 次猜中了！")
            break

玩猜数字()
玩猜数字()
玩猜数字()