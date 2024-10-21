menuList = []
systemMenu = {"ข้าวมันไก่ต้ม":45,"ข้าวมันไก่ทอด":45,"ข้าวมันไก่ทูโทน":55,"ข้าวหมกไก่":50,}

def showBill():
    sum = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        sum += menuList[number][1]
    print("Total Price :",sum,"บาท")


while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

showBill()