# Nhập tên và tuổi
Name = input('Nhập tên của bạn: ')
Age = int(input('Nhập tuổi của bạn: '))
if Age <= 10:
    print('Chào cháu ', Name)
elif 10 < Age <= 20:
    print('Chào bạn ', Name)
elif 20 < Age <= 50:
    print('Chào anh ', Name)
else:
    print('Chào bác ', Name)
