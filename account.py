record = []

while True:
    print("1 记账  2 看账本  3 退出 4 看总花费")
    choice = input("选哪个：")

    if choice == "1":
        item = input("记什么：")
        money = input("多少钱: ")
        record.append([item, int(money)])
        print("记好了！")
    elif choice == "2":
        for r in record:
            print(r)
    elif choice == "3":
        break
    elif choice == "4":
        total = 0
        for r in record:
                total = total + r[1]
        print("一共花了", total, "元")