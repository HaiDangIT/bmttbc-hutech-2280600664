def truycapphantu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

#nhap danh sach nguoi dung va xu ly
input_list = input("Nhap danh sach so: ")
numbers = list(map(int , input_list.split(' ')))

first , last = truycapphantu(numbers)

#in ket qua

print("In phan tu dau tien: ", first)

print("In phan tu cuoi cung: ", last)
 