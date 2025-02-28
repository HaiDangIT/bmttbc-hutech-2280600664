#Nhap cac dong tu nguoi dung
print ("Nhap cac dong van ban (Nhap 'done' de ket thuc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
    
    #Xu ly cac dong tu nguoi dung
    print("\nCac dong sau khi duoc xu ly in hoa: ")
for line in lines:
    print(line.upper())