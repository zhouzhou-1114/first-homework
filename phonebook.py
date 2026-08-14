phone = {}

def add_contact():
    name = input("名字: ")
    number = input("电话：")
    phone[name] = number
    print("已添加", name, "的电话！")

def find_contact():
    name = input("查谁: ")
    if name in phone :
        print(name,"的电话是", phone[name])
    else:
        print("通讯录里面没有", name)

while True:
    print("1 加联系人  2 查电话  3 退出")
    choice = input("选哪个: ")

    if  choice == "1":
        add_contact()
    elif choice == "2":
        find_contact()
    elif choice == "3":
        break