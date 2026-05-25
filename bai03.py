raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:
        choice = int(input("""
===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa dữ liệu và in báo cáo
3. Tìm kiếm nhân viên theo mã ID
4. Thoát chương trình
====================================
Nhập lựa chọn của bạn (1-4): 
"""))

        match choice:
            case 1:
                print(f"\n'{raw_data}'")
            case 2:

                employee_list = raw_data.split("|")

                print("\n================ BÁO CÁO NHÂN SỰ ================")

                print(f"ID:"
                      f"HỌ TÊN:"
                      f"SĐT:"
                      f"PHÒNG BAN:")
                print("-" * 70)
                for employee in employee_list:
                    data = employee.strip().split(";")
                    employee_id = data[0].strip().upper()
                    full_name = data[1].strip().title()
                    phone = data[2].strip().replace("-", "")
                    department = data[3].strip().upper()
                    if phone.isdigit():
                        phone = "******" + phone[-4:]
                    else:
                        phone = "Invalid Format"
                    print(f"{employee_id:<12}"
                          f"{full_name:<25}"
                          f"{phone:<20}"
                          f"{department:<15}")

            case 3:

                search_id = input("Nhập mã nhân viên cần tìm: ").strip().upper()
                employee_list = raw_data.split("|")
                for employee in employee_list:
                    data = employee.split(";")

                    employee_id = data[0].strip().upper()
                    full_name = data[1].strip().title()
                    phone = data[2].strip().replace("-", "")
                    department = data[3].strip().upper()

                    if phone.isdigit():
                        phone = "******" + phone[-4:]
                    else:
                        phone = "Invalid Format"
                    if employee_id == search_id:

                        print("\n===== THÔNG TIN NHÂN VIÊN =====")
                        print(f"ID         : {employee_id}")
                        print(f"Họ tên     : {full_name}")
                        print(f"SĐT        : {phone}")
                        print(f"Phòng ban  : {department}")
                        break
                    else:
                        print("Không tìm thấy nhân viên")

            case 4:
                print("Thoát chương trình")
                break

            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
