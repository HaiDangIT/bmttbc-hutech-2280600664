def tao_tuple_tulist(lst):
    return tuple(lst)

#nhap danh sach nguoi dung va xu ly chuoi
input_list = input("Nhap danh sach so va cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))

my_tuple =tao_tuple_tulist(numbers)
print ("List: " , numbers)
print ("Tuple tu List: ", my_tuple)