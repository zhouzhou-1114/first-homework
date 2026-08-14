record = []

def load():
    try:
        f =open("book.txt", "r")
        for line in f:
            parts = line.strip().split(" ")
            record.append([parts[0], int(parts[1])])
        f.close()
    except:
        print("第一次使用,还没有账目文件")

def save():
    f = open("book.txt", "w")
    for r in record:
        f.write(r[0] + " " + str(r[1]) + "\n")
    f.close()

def add_record():
    item = input("记什么: ")
    money = input("多少钱: ")
    record.append([item, int(money)])
    save()
    print("记好了！")

def show_records():
    for r in record:
        print(r[0], r[1], "元")
        
def show_total():
    total = 0
    for r in record:
        total = total + r[1]
    print("一共花了", total, "元")

load()

while True:
    print("1 记账 2 看账本 3 退出 4 看总花费")
    choice = input("选哪个： ")

    if choice == "1":
        add_record()
    elif choice == "2":
        show_records()
    elif choice == "3":
        break
    elif choice == "4":
        show_total()