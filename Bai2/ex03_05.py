def demsolanxuathien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] = +1
        else:
            count_dict[item] = 1
    return count_dict

#Nhap du lieu
input_list = input("Nhap danh sach chuoi ban muon: ")

word_list = input_list.split(' ')

print ("So lan xuat hien cua cac phan tu: ", demsolanxuathien(word_list))
