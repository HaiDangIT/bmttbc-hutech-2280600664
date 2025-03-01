def daonguoclist(lst):
    return lst[::-1]

#Nhap danh sach tu nguoi dung va xu ly chuoi 
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))

#dao nguoc chuoi va in ra
listdaonguoc = daonguoclist(numbers)
print("Chuoi da dao nguoc: ", listdaonguoc)
