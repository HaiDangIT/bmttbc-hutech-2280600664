from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("===============Menu=================")
    print("1. Them sinh vien.")
    print("2. Cap nhat thong tin sinh vien boi Id.")
    print("3. Xoa sinh vien boi Id.")
    print("4. Tim kiem sinh vien boi Id.")
    print("5. Sap xep sinh vien theo diem trung binh.")
    print("6. Sap xep sinh vien theo ten chuyen nganh.")
    print("7. Hien thi danh sach sinh vien.")
    print("0. Ket thuc chuong trinh.")
    print("=====================================")
    
    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("1.Them sinh vien")
        qlsv.nhapSinhVien()
        print("Them sinh vien thanh cong!")
    elif (key == 2):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n2.Cap nhat thong tin sinh vien.")
            print("\nNhap Id: ")
            Id = int(input())
            qlsv.updateSinhVien(Id)
        else:
            print("Danh sach sinh vien rong!")
    elif (key == 3):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n3.Xoa sinh vien.")
            print("\nNhap Id: ")
            Id = int(input())
            if (qlsv.deletebyId(Id)):
                print("Xoa sinh vien co Id = ", Id, "thanh cong!")
            else:
                print("Danh sach sinh vien rong!")
    elif (key == 4):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n4.Tim kiem sinh vien theo ten.")
            print("\nNhap ten de tim kiem: ")
            Name = input()
            searchResult = qlsv.findByName(Name)
            qlsv.showSinhVien(searchResult)
        else:
            print("Danh sach sinh vien rong!")
    elif (key == 5):
            if(qlsv.soLuongSinhVien() > 0):
                print("\n5.Sap xep sinh vien theo diem trung binh.")
                qlsv.sortByDiemTb()
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("Danh sach sinh vien rong!")
    elif (key == 6):
            if(qlsv.soLuongSinhVien() > 0):
                print("\n6.Sap xep sinh vien theo ten chuyen nganh.")
                qlsv.sortByMajor()
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("Danh sach sinh vien rong!")
    elif (key == 7):
            if(qlsv.soLuongSinhVien() > 0):
                print("\n7.Hien thi danh sach sinh vien.")
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("Danh sach sinh vien rong!")
    elif (key == 0):
            if(qlsv.soLuongSinhVien() > 0):
                print("\n0.Ban da chon ket thuc chuong trinh!")
                break
    else:
                    print("Khong co chuc nang nay!")
                    print("Hay chon chuc nang khac trong menu")