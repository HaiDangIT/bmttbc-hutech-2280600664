import json

list_dict = []

while True:
    list_dict_key = input("Enter key: ")

    if list_dict_key.lower() == 'stop':
        break
    
    list_dict_value = input("Enter value: ")

    list_dict.append({list_dict_key: list_dict_value})

# Print out the current list of dictionaries
print("Xuat danh sach: ", json.dumps(list_dict, indent=4))

def xoaphantu(dictionary, key):
    # Iterate over the list of dictionaries and remove any dictionary that has the key to delete
    for d in dictionary:
        if key in d:
            dictionary.remove(d)
            return True
    return False

input_del = input("Nhap key can xoa: ")

# Call the function to delete the element
result = xoaphantu(list_dict, input_del)
if result:
    print("Phan tu da duoc xoa tu Dictionary: ", json.dumps(list_dict, indent=4))
else:
    print("Khong tim thay phan tu can xoa!!!")
