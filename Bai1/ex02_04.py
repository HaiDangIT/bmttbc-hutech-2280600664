#tao 1 danh sach de luu
j=[]
#duyet tu 2000 den 3200 de tim so chi het cho 7 nhung khong la boi so cua 5
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))