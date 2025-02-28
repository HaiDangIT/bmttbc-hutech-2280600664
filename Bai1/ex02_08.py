#Ham kiem tra so nhi phan coo chia het cho 5 khong
def chiahetcho5(sonhiphan):
    #chuyen so nhi phan sang so thap phan
    sothaphan = int(str(sonhiphan), 2)
    #kiem tra so thap phan co chia het cho 5 khong
    if sothaphan % 5 == 0:
        return True
    else:
        return False
    
#nhap chuoi so nhi phan tu nguoi dung
chuoisonhiphan = input("Nhap chuoi so nhi phan(phan tach boi dau phay): ")
#tach chuoi so nhi phan
sonhiphanlist = chuoisonhiphan.split(',')
sochiahetcho5 = [so for so in sonhiphanlist if chiahetcho5(so)]
#in ra
if len(sochiahetcho5) > 0:
    ketqua = ',' .join(sochiahetcho5)
    print("Cac so chia het cho 5 la: ",ketqua)
else:
    print("Khong co so nao chia het cho 5") 