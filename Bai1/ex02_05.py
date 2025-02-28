sogiolam = float(input("Nhap so gio lam moi tuan: "))
luonggio = float(input("Nhap so thu lao cho moi gio: "))
giotieuchuan = 44
giovuotchuan = max(0 , sogiolam - giotieuchuan)
luong = giotieuchuan * luonggio + giovuotchuan * luonggio *1.5
print(f"Luong cua ban la: {luong}")