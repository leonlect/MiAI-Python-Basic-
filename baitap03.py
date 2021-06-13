# Nhap vao nhiet do va don vi C/F neu la C thi bo qua
temp = int(input('Nhập nhiệt độ: '))
dv = input('Nhập đơn vị: ')
if dv == 'C' or dv == 'c':
    print('Nhiệt độ là ', temp, 'độ C')
elif dv == 'F' or dv == 'f':
    #c = 1
    c = ((temp-32) * 5) // 9
    print('Nhiệt độ sau khi đổi từ F sang C là ', c, ' độ C')
else:
    print('Bạn phải nhập đơn vị F hoặc C !')
