def tinhtongchan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

#nhap danh sach tu nguoi dung va chuoi
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))

#tinh toan
tongchan = tinhtongchan(numbers)
print("Tong so chan trong list la: ", tongchan)
