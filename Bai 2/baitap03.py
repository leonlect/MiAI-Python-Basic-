def kgToGam():
    print("Nhập số kg cần đổi: ")
    kg = int(input())
    return kg * 1000


def mToMM():
    print("Nhập số m cần đổi: ")
    m = int(input())
    return m * 1000


print('--------------')
print('|    MENU    |')
print('--------------')
print("0 - Thoát")
print("1 - Đổi từ kg sang gam")
print("2 - Đổi từ m sang mm")
menu = int(input("Chọn 1 chức năng: "))
if menu == 1:
    g = kgToGam()
    print(g, "gam")
elif menu == 2:
    print(mToMM())
else:
    print("Cám ơn sử dụng Menu !")
