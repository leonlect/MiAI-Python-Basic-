num = int(input('Nhập 1 số: '))
while num % 2 != 0:
    if(num % 2 == 0):
        break
    num = int(input('Nhập lại: '))
print(num, " chia het cho 2")
