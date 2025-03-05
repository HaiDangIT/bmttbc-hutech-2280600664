from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    
    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if(maxId < sv._id):
                    maxId = sv._id
                maxId = maxId + 1
            return maxId
        
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    
    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh cua sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTb = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svId, name, sex , major, diemTb)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        
    def updateSinhVien(self, Id):
        sv:SinhVien = self.findByID(Id)
        if(sv != None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            diemTb = float(input("Nhap diem cua sinh vien: "))
            
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTb = diemTb
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co Id = {} khong ton tai." .format(Id))
            
    def sortById(self):
        self.listSinhVien.sort(key=lambda x: x._id, reversed=False)
    
    def sortByMajor(self):
        self.listSinhVien.sort(key=lambda x: x._major, reversed=False)
            
    def sortByDiemTb(self):
        self.listSinhVien.sort(key=lambda x: x._diemTb, reversed=False)
    
    def findById(self, Id):
        searchResult = None
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                
                if (sv._id == Id):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deletebyId(self, Id):
        isDeleted = False
        sv = self.findById(Id)
        if(sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLyc(self, sv:SinhVien):
        if sv._diemTb >= 8:
            sv._hocLuc ="Gioi"
        elif sv._diemTb >= 6.5:
            sv._hocLuc = "Kha"
        elif sv._diemTb >= 5:
            sv._hocLuc = "Trung binh"
        else: 
            sv._hocLuc = "Yeu"
            
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}"
              .format("Id","Name" , "Sex", "Major", "Diem Tb", "Hoc Luc"))
        
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}"
                .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTb, sv._hocLuc))
                
        print("\n")
        
    def getListSinhVien(self):
        return self.listSinhVien
    
    
    