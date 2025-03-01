# class Mydict:
#     def nhapphantu (dict):
#         dict.key = input("Enter key: ")
#         dict.value = input("Enter value: ")
def xoaphantu (dictionary,key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False


    #su dung ham va in ket qua
    
input_list = int(input("Nhap so key ban muon tao: "))

list_dict = {input("Enter key: "): input("Enter value: ") for _ in range(input_list)}

input_del = input("Nhap key can xoa: ")

result = xoaphantu(list_dict,input_del)
if result:
    print ("Phan tu da duoc xoa tu Dictionary: ", list_dict)
else:
    print ("Khong tim thay phan tu can xoa!!!")


    
